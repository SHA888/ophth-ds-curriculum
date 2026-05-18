"""Load a JPEG fundus image, inspect its shape and dtype, and perform a round‑trip save.

This script demonstrates the basics of handling fundus images as NumPy ndarrays.
It is used by the *01‑ndarray‑exercise.qmd* Quarto document.
"""

import pathlib
import sys

# Try to import image handling libraries; fall back gracefully if missing.
try:
    import imageio.v3 as iio  # imageio v3 API
except Exception:  # pragma: no cover
    try:
        import imageio as iio
    except Exception as e:
        sys.stderr.write(f"Failed to import imageio: {e}\n")
        sys.exit(1)


def main(image_path: str | pathlib.Path = "sample-fundus.jpg") -> None:
    """Load *image_path*, print its shape and dtype, and save a PNG round‑trip.

    Parameters
    ----------
    image_path: str or pathlib.Path, optional
        Path to the JPEG fundus image. Defaults to ``sample-fundus.jpg`` in the
        same directory as this script.
    """
    img_path = pathlib.Path(image_path)
    if not img_path.is_file():
        sys.stderr.write(f"Image not found: {img_path}\n")
        sys.exit(1)

    # Load the image as a NumPy array (H, W, C) with dtype uint8.
    arr = iio.imread(img_path)
    print(f"Loaded {img_path.name}: shape={arr.shape}, dtype={arr.dtype}")

    # Save a round‑trip PNG.
    png_path = img_path.with_suffix(".png")
    iio.imwrite(png_path, arr)
    print(f"Saved round‑trip PNG to {png_path.name}")

    # Reload the PNG and verify shape/dtype.
    arr_png = iio.imread(png_path)
    print(f"Reloaded PNG: shape={arr_png.shape}, dtype={arr_png.dtype}")
    if arr.shape == arr_png.shape and arr.dtype == arr_png.dtype:
        print("Round‑trip verification succeeded.")
    else:
        print("Warning: shape or dtype changed after round‑trip.")


if __name__ == "__main__":
    # Allow a custom path via command line argument.
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
