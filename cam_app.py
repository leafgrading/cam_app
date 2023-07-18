import streamlit as st
from PIL import Image
import math

def show_image_with_text(image, text=None):
    st.image(image, use_column_width=True)
    if text is not None:
        st.text("")
        if text.startswith("Rejected"):
            st.error(text)
        elif text.startswith("Accepted"):
            st.success(text)
        else:
            st.info(text)


def show_five_images(uploaded_images, text=None):
    num_columns = 3

    # Calculate the width of each column
    column_width = math.floor(12 / num_columns)
    for i, image in enumerate(uploaded_images):
        # Display image in a card-like layout within a column
        if i % num_columns == 0:
            col = st.columns(num_columns)

        # image = image.resize((256, 320))
        with col[i % num_columns]:
            if text is None:
                show_image_with_text(image, None)
            else:
                show_image_with_text(image, text[i])

def main():
    st.title("Camera input demo")
    # st.write(st.session_state)
    capture_images = []
    if "cam_state" not in st.session_state:
        st.session_state.cam_state = False
        st.session_state.cap_count = 0
    # if st.session_state.cap_count == 5:
    #     st.session_state.cam_state = True
    picture1 = st.camera_input(label="Camera1", key="1st Image")
    if picture1:
        capture_images.append(picture1)
    picture2 = st.camera_input(label="Camera2", key="2nd Image")
    if picture2:
        capture_images.append(picture2)
    picture3 = st.camera_input(label="Camera3", key="3rd Image")
    if picture3:
        capture_images.append(picture3)
    picture4 = st.camera_input(label="Camera4", key="4th Image")
    if picture4:
        capture_images.append(picture4)
    picture5 = st.camera_input(label="Camera5", key="5th Image")
    if picture5:
        capture_images.append(picture5)
    if len(capture_images) > 0:
        show_five_images(capture_images)

if __name__ == "__main__":
    main()
