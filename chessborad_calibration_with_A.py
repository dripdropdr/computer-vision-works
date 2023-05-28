import numpy as np
import cv2 as cv


def calib_camera_from_chessboard(input_file, board_pattern, board_cellsize, select_all=False, wait_msec=10, K=None, dist_coeff=None, calib_flags=None):

    video = cv.VideoCapture(input_file)
    
    # Select images
    img_select = []
    img_points = []
    while True:
        # Grab an images from the video
        valid, img = video.read()
        if not valid:
            break

        if select_all:
            img_select.append(img)
            # Find 2D corner points from given images
            complete, pts = cv.findChessboardCorners(img, board_pattern)
            if complete:
                img_points.append(pts)
        else:
            # Show the image
            display = img.copy()
            cv.putText(display, f'NSelect: {len(img_select)}', (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (0, 255, 0))
            cv.imshow('Camera Calibration', display)

            # Process the key event
            key = cv.waitKey(wait_msec)
            if key == 27:                  # 'ESC' key: Exit (Complete image selection)
                break
            elif key == ord(' '):          # 'Space' key: Pause and show corners
                # Find 2D corner points from given images
                complete, pts = cv.findChessboardCorners(img, board_pattern)
                cv.drawChessboardCorners(display, board_pattern, pts, complete)
                cv.imshow('Camera Calibration', display)
                key = cv.waitKey()
                if key == 27: # ESC
                    break
                elif key == ord('\r'):
                    img_select.append(img) # 'Enter' key: Select the image
                    if complete:
                        img_points.append(pts)

    cv.destroyAllWindows()
    assert len(img_points) > 0, 'There is no set of complete chessboard points!'

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Prepare 3D points of the chess board
    obj_pts = [[c, r, 0] for r in range(board_pattern[1]) for c in range(board_pattern[0])]
    obj_points = [np.array(obj_pts, dtype=np.float32) * board_cellsize] * len(img_points) # Must be 'np.float32'

    # Calibrate the camera
    return cv.calibrateCamera(obj_points, img_points, gray.shape[::-1], K, dist_coeff, flags=calib_flags)


def pose_estimation(input_file, board_pattern, board_cellsize, K, dist_coeff):
    # The given video and calibration data
    board_criteria = cv.CALIB_CB_ADAPTIVE_THRESH + cv.CALIB_CB_NORMALIZE_IMAGE + cv.CALIB_CB_FAST_CHECK

    # Open a video
    video = cv.VideoCapture(input_file)
    assert video.isOpened(), 'Cannot read the given input, ' + input_file

    # Prepare a 3D box for simple AR
    box_lower = board_cellsize * np.array([[2, 2, 0], [3, 2, -1]])
    box_upper = board_cellsize * np.array([[4, 2, 0], [3, 2, -1]])

    # Prepare 3D points on a chessboard
    obj_points = board_cellsize * np.array([[c, r, 0] for r in range(board_pattern[1]) for c in range(board_pattern[0])])

    # Run pose estimation
    while True:
        # Read an image from the video
        valid, img = video.read()
        if not valid:
            break

        # Estimate the camera pose
        complete, img_points = cv.findChessboardCorners(img, board_pattern, board_criteria)
        if complete:
            ret, rvec, tvec = cv.solvePnP(obj_points, img_points, K, dist_coeff)

            # Draw the box on the image
            line_lower, _ = cv.projectPoints(box_lower, rvec, tvec, K, dist_coeff)
            line_upper, _ = cv.projectPoints(box_upper, rvec, tvec, K, dist_coeff)
            cv.polylines(img, [np.int32(line_lower)], True, (255, 0, 0), 2)
            cv.polylines(img, [np.int32(line_upper)], True, (0, 0, 255), 2)
            cv.line(img, np.int32(line_lower.sum(axis=0).flatten()/2), np.int32(line_upper.sum(axis=0).flatten()/2), (0, 255, 0), 2)

            # Print the camera position
            R, _ = cv.Rodrigues(rvec) # Alternative) scipy.spatial.transform.Rotation
            p = (-R.T @ tvec).flatten()
            info = f'XYZ: [{p[0]:.3f} {p[1]:.3f} {p[2]:.3f}]'
            cv.putText(img, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (0, 255, 0))

        # Show the image and process the key event
        cv.imshow('Pose Estimation (Chessboard)', img)
        key = cv.waitKey(10)
        if key == ord(' '):
            key = cv.waitKey()
        if key == 27: # ESC
            break


    video.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    input_file = './hw3/IMG_1515.MOV'
    board_pattern = (8, 6)
    board_cellsize = 0.03

    rms, K, dist_coeff, rvecs, tvecs = calib_camera_from_chessboard(input_file, board_pattern, board_cellsize)

    pose_estimation(input_file, board_pattern, board_cellsize, K, dist_coeff)

    # Print calibration results
    print('## Camera Calibration Results')
    # print(f'* The number of selected images = {len(img_select)}')ㅊ
    print(f'* RMS error = {rms}')
    print(f'* Camera matrix (K) = \n{K}')
    print(f'* Distortion coefficient (k1, k2, p1, p2, k3, ...) = {dist_coeff.flatten()}')