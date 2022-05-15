# Problems Encountered

- Resizing broke the coordinates of the canvas
  - The problem was resolved by manually setting the image alignment
- Resizing did not properly change the image size
  - The problem was resolved by manually resizing the image by overloading the resizeEvent function
- Resizing the application made the widgets too large
  - The problem was resolved by setting fixed dimensions to the minimum possible calculated by PyQt
