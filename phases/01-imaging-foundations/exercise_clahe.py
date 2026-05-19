"""Exercise: Compare CLAHE implementations across scikit-image and OpenCV.

This script demonstrates two standard-library implementations of Contrast Limited
Adaptive Histogram Equalization (CLAHE) on a fundus image:

1. **scikit-image** via ``exposure.equalize_adapthist`` (reference implementation).
2. **OpenCV** via ``cv2.createCLAHE`` (production-grade, optimized).

The script loads an RGB fundus image, applies both methods with equivalent parameters,
compares results side-by-side, and computes MSE to verify consistency.
"""

import pathlib
import sys

import numpy as np

# Try to import required libraries; exit with a clear message if missing.
try:
    import imageio.v3 as iio
except Exception:  # pragma: no cover
    try:
        import imageio as iio
    except Exception as e:
        sys.stderr.write(f"Failed to import imageio: {e}\n")
        sys.exit(1)

try:
    import cv2  # OpenCV
except Exception as e:  # pragma: no cover
    sys.stderr.write(f"Failed to import OpenCV (cv2): {e}\n")
    sys.exit(1)

try:
    from skimage import exposure
except Exception as e:  # pragma: no cover
    sys.stderr.write(f"Failed to import scikit-image: {e}\n")
    sys.exit(1)


def apply_clahe_skimage(
    image: np.ndarray, clip_limit: float = 2.0, tile_grid_size: int = 8
) -> np.ndarray:
    """Apply CLAHE using scikit-image's ``equalize_adapthist``.

    Parameters
    ----------
    image: np.ndarray
        Input image in ``uint8`` format (H, W, C).
    clip_limit: float, optional
        Clipping threshold. Normalized as a fraction of histogram range by scikit-image.
        Default 2.0 (expressed as a percentage, internally divided by 100).
    tile_grid_size: int, optional
        Size of the tile grid. Default 8 (i.e., 8×8 tiles).
    """
    img_float = image.astype(np.float32) / 255.0
    channels = []
    for c in range(img_float.shape[2]):
        ch = exposure.equalize_adapthist(
            img_float[..., c],
            clip_limit=clip_limit
            / 100.0,  # scikit-image normalizes: expects fraction in [0, 1]
            kernel_size=tile_grid_size,
        )
        channels.append(ch)
    result = np.stack(channels, axis=-1)
    return (result * 255).astype(np.uint8)


def apply_clahe_opencv(
    image: np.ndarray, clip_limit: float = 2.0, tile_grid_size: int = 8
) -> np.ndarray:
    """Apply CLAHE using OpenCV's ``cv2.createCLAHE``.

    Parameters
    ----------
    image: np.ndarray
        Input image in ``uint8`` format (H, W, C).
    clip_limit: float, optional
        Absolute clipping threshold in pixel value counts (not normalized).
        OpenCV interprets this as the max height allowed in any histogram bin.
        Default 2.0.
    tile_grid_size: int, optional
        Size of the tile grid. Default 8 (i.e., 8×8 tiles).

    Notes
    -----
    OpenCV's clipLimit uses absolute pixel counts, while scikit-image normalizes
    as a fraction of histogram range. To make them roughly equivalent, we use the
    same numeric value (2.0) for both, but be aware the semantics differ slightly.
    """
    clahe = cv2.createCLAHE(
        clipLimit=clip_limit, tileGridSize=(tile_grid_size, tile_grid_size)
    )
    channels = [clahe.apply(image[..., i]) for i in range(image.shape[2])]
    return np.stack(channels, axis=-1)


def main(image_path: str | pathlib.Path = "sample-fundus.jpg") -> None:
    img_path = pathlib.Path(image_path)
    if not img_path.is_file():
        sys.stderr.write(f"Image not found: {img_path}\n")
        sys.exit(1)

    img = iio.imread(img_path)
    if img.ndim != 3 or img.shape[2] != 3:
        sys.stderr.write("Expected an RGB image with 3 channels.\n")
        sys.exit(1)

    skimage_result = apply_clahe_skimage(img)
    opencv_result = apply_clahe_opencv(img)

    # Compute MSE between the two CLAHE implementations.
    mse = np.mean(
        (skimage_result.astype(np.float32) - opencv_result.astype(np.float32)) ** 2
    )
    print(f"MSE between scikit-image and OpenCV CLAHE: {mse:.2e}")

    # Stack results horizontally for visual comparison.
    comparison = np.concatenate([img, skimage_result, opencv_result], axis=1)
    out_path = img_path.with_name("clahe_comparison.png")
    iio.imwrite(out_path, comparison)
    print(
        f"Saved CLAHE comparison image to {out_path}\nLayout: [Original | scikit-image | OpenCV]"
    )


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
