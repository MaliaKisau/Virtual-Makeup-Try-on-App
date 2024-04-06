# Function to load and display the user's photo
def load_photo():
    filepath = filedialog.askopenfilename()
    if filepath:
        img = cv2.imread(filepath)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)
        label.config(image=img)
        label.image = img
