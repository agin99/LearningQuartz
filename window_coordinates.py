import Quartz
import sys

# Get the coordinates of specific window

def get_window_type_information(windows, window_title):
    window_information_list = []
    for index, window in enumerate(windows):
        if window['kCGWindowOwnerName'] == window_title:
            window_information_dict = {
                'title' : '',
                'top_left' : (0, 0),
                'top_right' : (0, 0),
                'bottom_left' : (0, 0),
                'bottom_right' : (0, 0)
            }
            height = window['kCGWindowBounds']['Height']
            width = window['kCGWindowBounds']['Width']
            x = window['kCGWindowBounds']['X']
            y = window['kCGWindowBounds']['Y']
            window_information_dict['title'] = window_title
            window_information_dict['top_left'] = (x, y)
            window_information_dict['top_right'] = (x + width, y)
            window_information_dict['bottom_left'] = (x, y + height)
            window_information_dict['bottom_right'] = (x + width, y + height)
            window_information_list.append(window_information_dict)
    return window_information_list


def main(application_name):
    windows = Quartz.CGWindowListCopyWindowInfo(Quartz.kCGWindowListOptionOnScreenOnly, Quartz.kCGNullWindowID)

    window_information_list = get_window_type_information(windows, application_name)
    for window in window_information_list:
        print(window)

if __name__ == "__main__":
    arg1 = sys.argv[1]
    print(f"Getting window information for {arg1}...")
    main(sys.argv[1])
