import streamlit as st
from PIL import Image
import math
from streamlit_back_camera_input import back_camera_input

def show_image_with_text(image, text=None):
    st.markdown('<div class="image-row">', unsafe_allow_html=True)
    st.image(image, use_column_width=True)
    if text is not None:
        st.text("")
        if text.startswith("Rejected"):
            st.error(text)
        elif text.startswith("Accepted"):
            st.success(text)
        else:
            st.info(text)
    st.markdown('</div>', unsafe_allow_html=True)

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

def show_five_images2(uploaded_images, text=None):
    num_columns = 5

    # Calculate the width of each column
    col_width = st.columns(num_columns)
    for i, image in enumerate(uploaded_images):
        # Display image in a card-like layout within a column
        col = col_width[i]
        
        image = image.resize((256, 320))
        with col:
            if text is None:
                show_image_with_text(image, None)
            else:
                show_image_with_text(image, text[i])
    

def change_state():
    st.session_state.cap_count += 1
    if st.session_state.cap_count == 10:
        st.session_state.cam_state = True

def main():
    # st.title("Camera input demo")
    with open("custom.css") as css:
        st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)
    # with open("header.html") as head:
    #     st.markdown(f"<html>{head.read()}</html>", unsafe_allow_html=True)
    # st.write(st.session_state)
    # Add a custom CSS style to set the background color of the header to white
    col1, col2, col3 = st.columns([1, 3, 1])

    # Logo on the left side
    with col1:
        st.image("BAT_Bangladesh_Logo.png", width=100)  # Replace "left_logo.png" with the path to your left logo image

    # Main heading in the center
    with col2:
        st.title("Leaf Grading")

    # Logo on the right side
    with col3:
        st.image("RedDot-Logo.png", width=100)  # Replace "right_logo.png" with the path to your right logo image


    capture_images = []
    if "cam_state" not in st.session_state:
        st.session_state.cam_state = False
        st.session_state.cap_count = 0
    picture = None
    # if st.session_state.cam_state != True:
    # Toggle button for the camera
    st.subheader("Choose an option:")
    option = st.radio("", ("Upload Image File", "Capture Image"))
    if option == "Upload Image File":
        uploaded_file = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"], accept_multiple_files=True)
        if uploaded_file is not None:
            for file in uploaded_file:
                if len(capture_images) >= 5:
                    break
                image = Image.open(file)
                capture_images.append(image)
                st.session_state.cam_state = True
    elif option == "Capture Image":
        picture = st.camera_input(label="Camera Input", on_change= change_state(), disabled=st.session_state.cam_state, key="photo1")
    if picture or st.session_state.cam_state == True:
        # st.session_state.cap_count += 1
        if len(capture_images)>0:
            st.session_state.images = capture_images
        else:
            if picture is not None:
                picture = Image.open(picture)
            if "images" not in st.session_state:
                capture_images.append(picture)
                st.session_state.images = capture_images
            else:
                capture_images = st.session_state.images
                if picture is not None:
                    capture_images.append(picture)
                    st.session_state.images = capture_images
        # st.write(len(st.session_state.images))
        st.subheader("Original Image Preview")
        show_five_images2(st.session_state.images,None)
        st.markdown("___")
        if len(st.session_state.images) >= 5:
            st.subheader("Preview (background removed)")
            val_result = ["Accepted(72%)","Accepted(72%)","Rejected","Accepted(72%)","Rejected"]
            show_five_images2(st.session_state.images,None)
            st.markdown("___")
            # st.subheader("Grading")
            button1 = st.button('Validate')
            if st.session_state.get('button') != True:
                st.session_state['button'] = button1
            if st.session_state['button'] == True:
                st.subheader("Validation Result")
                show_five_images2(st.session_state.images,val_result)
                print("Validation Print Hobe")
                st.markdown("___")
                pred_button_pressed = st.button("Predict")
                predicted_result = ["MDA", "MDA", "POA", "MDA", "MOA"]
                if pred_button_pressed:
                    st.subheader("Prediction Result")
                    show_five_images2(st.session_state.images[:3], predicted_result[:3])
                    st.markdown("___")
                    st.subheader("Overall Grade")
                    st.info("MDA")
                    st.subheader("Predicted Price")
                    st.info("195")

if __name__ == "__main__":
    main()


