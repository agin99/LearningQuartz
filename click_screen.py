import Quartz
import sys
import window_coordinates

def left_click_screen(x, y):
    left_click = Quartz.CGEventCreateMouseEvent(None, Quartz.kCGEventLeftMouseDown, (x, y), Quartz.kCGMouseButtonLeft)
    Quartz.CGEventPost(Quartz.kCGHIDEventTap, left_click)

    left_release = Quartz.CGEventCreateMouseEvent(None, Quartz.kCGEventLeftMouseUp, (x, y), Quartz.kCGMouseButtonLeft)
    Quartz.CGEventPost(Quartz.kCGHIDEventTap, left_release)

def right_click_screen(x, y): 
    right_click = Quartz.CGEventCreateMouseEvent(None, Quartz.kCGEventRightMouseDown, (x, y), Quartz.kCGMouseButtonRight)
    Quartz.CGEventPost(Quartz.kCGHIDEventTap, right_click)

    right_release = Quartz.CGEventCreateMouseEvent(None, Quartz.kCGEventRightMouseUp, (x, y), Quartz.kCGMouseButtonRight)
    Quartz.CGEventPost(Quartz.kCGHIDEventTap, right_release)

def main(window, click_type, x, y):
    if click_type == 'left':
        left_click_screen(x, y)    
    elif click_type == 'right':
        right_click_screen(x, y)

if __name__ == "__main__":
    windows = Quartz.CGWindowListCopyWindowInfo(Quartz.kCGWindowListOptionOnScreenOnly, Quartz.kCGNullWindowID)
    window = window_coordinates.get_window_type_information(windows, sys.argv[1])[1]
    x, y = window['top_left']
    x += 50
    y += 50
    main(window, sys.argv[2], x, y)