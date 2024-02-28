from openride import AsciiViewer, BoundingBox, Point, SubCategory, Size


if __name__ == "__main__":

    box = BoundingBox(size=Size(2,1,1))

    v = AsciiViewer()

    v.camera.set_position(Point(-8, 0, 2))

    while True:

        box.rotation.yaw += 0.01

        v.draw_model(SubCategory.Car, box, color=(1,0.3,0.3))

        v.update()
