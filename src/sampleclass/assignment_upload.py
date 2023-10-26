def handle_uploaded_file(f,user):

    print("File uploaded by user")
    print(user)
    with open("sampleclass/uploaded_files/assignment1.txt", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)