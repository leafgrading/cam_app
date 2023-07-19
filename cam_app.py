import streamlit as st
from PIL import Image
import math
from streamlit_back_camera_input import back_camera_input

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

def change_state():
    st.session_state.cap_count += 1
    if st.session_state.cap_count == 10:
        st.session_state.cam_state = True

def main():
    st.title("Camera input demo")
    # st.write(st.session_state)
    capture_images = []
    if "cam_state" not in st.session_state:
        st.session_state.cam_state = False
        st.session_state.cap_count = 0
    # picture = None
    # if st.session_state.cam_state != True:
    picture = st.camera_input(label="Camera", on_change= change_state(), disabled=st.session_state.cam_state, key="photo1")
    if picture or st.session_state.cam_state == True:
        # st.session_state.cap_count += 1

        if "images" not in st.session_state:
            capture_images.append(picture)
            st.session_state.images = capture_images
        else:
            capture_images = st.session_state.images
            if picture is not None:
                capture_images.append(picture)
                st.session_state.images = capture_images
        # st.write(len(st.session_state.images))
        if len(st.session_state.images) >= 5:
            st.session_state.cam_state = True
            show_five_images(st.session_state.images,None)

if __name__ == "__main__":
    main()


# import streamlit as st

# def take_camera_input():
#   """Takes a picture from the user's webcam and returns it as an image."""
#   image = st.camera_input("Take a picture")
#   return image

# def disable_camera():
#   """Disables the user's webcam."""
#   st.camera_input("", disabled=True)

# if __name__ == "__main__":
#   # Take a picture from the user's webcam.
#   image = take_camera_input()

#   # Display the image on the Streamlit page.
#   st.image(image)

#   # If the user clicks on the "Take a picture" button, disable the webcam.
#   if st.button("Disable Camera"):
#     disable_camera()

#   # Disable the webcam on change method.
#   st.camera_input("", on_change=disable_camera)


