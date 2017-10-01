

def createGallery(client, s3client, imagesBucket):

    print("Creating image gallery...")
    theObjects = s3client.list_objects(Bucket=imagesBucket)['Contents']

    #
    # delete previous collection, if any
    try:
        client.delete_collection(
            CollectionId = 'Gallery'
        )
    except Exception:
        pass


    # Create a collection using images in S3
    client.create_collection(
        CollectionId='Gallery',
        )
        
    for image in theObjects:

        fileName = image["Key"]
        imageId = fileName.split(".")[0]        

        client.index_faces(
            CollectionId='Gallery',
            Image={
                'S3Object': {
                    'Bucket': imagesBucket,
                    'Name': fileName
                }
            },
            ExternalImageId= imageId,
            DetectionAttributes=['DEFAULT']
            )

    print("...Created gallery.")
        
