import cv2
from cv2 import UMat

def draw_arrowed_crosshair(frame:UMat, center, color, thickness, size:list=[200,80]):
    h, w = frame.shape[:2]
    # Crosshair boyutları
    rect_width = size[0]
    rect_height = size[1]
    line_length = 25

    # Dikdörtgenin dört köşesini hesaplayalım
    top_left = (w // 2 - rect_width, h // 2 - rect_height)
    top_right = (w // 2 + rect_width, h // 2 - rect_height)
    bottom_left = (w // 2 - rect_width, h // 2 + rect_height)
    bottom_right = (w // 2 + rect_width, h // 2 + rect_height)

    # Dikdörtgenin köşelerine çizgiler çizelim
    cv2.line(frame, top_left, (top_left[0], top_left[1] + line_length), color, thickness)
    cv2.line(frame, top_left, (top_left[0] + line_length, top_left[1]), color, thickness)

    cv2.line(frame, top_right, (top_right[0], top_right[1] + line_length), color, thickness)
    cv2.line(frame, top_right, (top_right[0] - line_length, top_right[1]), color, thickness)

    cv2.line(frame, bottom_left, (bottom_left[0], bottom_left[1] - line_length), color, thickness)
    cv2.line(frame, bottom_left, (bottom_left[0] + line_length, bottom_left[1]), color, thickness)

    cv2.line(frame, bottom_right, (bottom_right[0], bottom_right[1] - line_length), color, thickness)
    cv2.line(frame, bottom_right, (bottom_right[0] - line_length, bottom_right[1]), color, thickness)
    return frame

def add_hud(frame:UMat, topic_text='SYSTEM',problem_status = 'TRACKER PROBLEM: False', top_middle_text="HUD", roll='0', pitch='0', fps='0',
                font = cv2.FONT_HERSHEY_SIMPLEX,font_scale = 0.7, font_thickness = 3, line_thickness = 2, crosshair_lenght=40):
    green_color = (0, 255, 0)
    red_color = (0, 0, 255)
    image_height, image_width, _ = frame.shape

    # Frame resize
    frame = cv2.resize(frame, (720,1280))

    # Adding green topic text at the top left corner
    cv2.putText(frame, topic_text, (20, 40), font, font_scale, green_color, font_thickness)

    # Text under topic
    cv2.putText(frame, problem_status, (20, 70), font, font_scale, green_color, font_thickness)

    # Add elements at the top in the middle
    text_size = cv2.getTextSize(top_middle_text, font, font_scale, font_thickness)[0]
    text_x = (image_width - text_size[0]) // 2
    text_y = 40
    cv2.putText(frame, top_middle_text, (text_x, text_y), font, font_scale, green_color, font_thickness)

    # Draw a crosshair in the middle with rectangle corners
    center_x, center_y = image_width // 2, image_height // 2
    frame = self.draw_arrowed_crosshair(frame, (center_x, center_y), green_color, 2)

    # Draw a dot in the middle
    cv2.circle(frame, (center_x, center_y), 3, green_color, -1)
    # Draw lines in three directions
    cross_gap = 15
    cv2.line(frame, (center_x-cross_gap, center_y), (center_x - line_length, crosshair_lenght, center_y), green_color, line_thickness)  # left
    cv2.line(frame, (center_x+cross_gap, center_y), (center_x + line_length, crosshair_lenght, center_y), green_color, line_thickness)  # right
    cv2.line(frame, (center_x, center_y+cross_gap), (center_x, center_y + line_length, crosshair_lenght), green_color, line_thickness)  # bottom
    return frame
    