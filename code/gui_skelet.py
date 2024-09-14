import dearpygui.dearpygui as dpg
from interface_skelet import title1, title2, timed_display, loadfile, display_options
import lib_skelet
import helpers


raw_array = None
filename = None
path = None
raw_img = None


def file_callback(sender, app_data):
    global raw_array
    raw_array = helpers.helper_loader(sender, app_data)


def image_enqueue(sender, app_data):
    helpers.helper_imager(sender)


def image_save(sender, app_data):
    helpers.helper_save()


def create_windows():

    with dpg.window(
        label="file", no_close=True, collapsed=True, no_move=True, no_resize=True
    ):
        dpg.add_button(
            label="load raw file", callback=lambda: dpg.show_item("file_dialog_id")
        )
        dpg.add_button(label="save as png", callback=image_save)
        dpg.add_button(label="quit", callback=dpg.stop_dearpygui)

    with dpg.file_dialog(
        directory_selector=False,
        show=False,
        callback=file_callback,
        id="file_dialog_id",
        width=700,
        height=400,
    ):
        dpg.add_file_extension(".*", color=(150, 255, 150, 255))  # Allow all file types

    with dpg.window(
        label="help",
        collapsed=True,
        no_close=True,
        no_move=True,
        no_resize=True,
        pos=(120, 0),
    ):
        dpg.add_button(label="how to use", callback=lambda: dpg.show_item("how_to_use"))
        dpg.add_button(label="readme")
        dpg.add_button(label="credits", callback=lambda: dpg.show_item("credits"))

    with dpg.window(
        no_close=True,
        no_move=True,
        no_resize=True,
        pos=(25, 110),
        no_background=True,
        no_title_bar=True,
    ):
        dpg.add_button(
            label="full rgbg", width=160, height=50, pos=(0, 0), callback=image_enqueue
        )
        dpg.add_button(
            label="full rgba", width=160, height=50, pos=(0, 70), callback=image_enqueue
        )
        dpg.add_button(
            label="bw from r channel",
            width=160,
            height=50,
            pos=(0, 140),
            callback=image_enqueue,
        )
        dpg.add_button(
            label="bw from g channels",
            width=160,
            height=50,
            pos=(0, 210),
            callback=image_enqueue,
        )
        dpg.add_button(
            label="bw from b channel",
            width=160,
            height=50,
            pos=(0, 280),
            callback=image_enqueue,
        )

    with dpg.window(
        no_close=True,
        show=False,
        id="credits",
        no_move=True,
        no_resize=True,
        pos=(200, 180),
        no_background=True,
        no_title_bar=True,
        height=400,
        width=750,
    ):
        dpg.add_text(title1())
        dpg.add_text(title2())

    with dpg.window(
        no_close=True,
        show=False,
        id="how_to_use",
        no_move=True,
        no_resize=True,
        pos=(200, 110),
        no_background=True,
        no_title_bar=True,
        height=400,
        width=750,
    ):
        dpg.add_text(
            "* file -> 'load raw file' to choose which photo to process\n* then choose a display method\n* to save close the image window and do 'file -> save as png'"
        )


def main():
    dpg.create_context()
    dpg.create_viewport(title="skelet", width=700, height=470)
    create_windows()
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == "__main__":
    main()
