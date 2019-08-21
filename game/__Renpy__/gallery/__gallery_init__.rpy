init python:
    from shutil import copyfile
    import time
    
    if persistent.gallery_votes is None:
        # key is id and value is a string for upvote, netrual, downvote
        persistent.gallery_votes = {}
    
    def create_folder_if_not_exist(path):
        #Create the folder if it dont exist
        try:
            os.makedirs(path)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
    
    def outfit_cached(file_info):
        char = file_info[4]
        file_name = str(file_info[0]) + file_info[1].split("/",-1)[-1]
        file_path = config.basedir+"\\game\\outfits\\"+char.lower()+"\\"+file_name
        if not os.path.isfile(file_path):
            headers = { 'User-Agent' : 'Mozilla/5.0' }
            response = urllib2.urlopen(urllib2.Request(file_info[1], None, headers)).read()
            #Write the file to a folder in outfits under the characters name 
            #With the file name of ImageID + ImageName
            f = open(file_path, "wb+")
            f.write(response)
            f.close()
            
    def get_request(url, header=None):
        opener = urllib2.build_opener(urllib2.HTTPHandler)
        req = urllib2.Request(url)
        req.add_header('Content-Type', 'application/json')
        req.add_header('Authorization', 'Basic ')
        if not header == None:
            req.add_header(header[0], header[1]) 
        req.get_method = lambda: 'GET'
        resualt = opener.open(req)
        # need to be read in the python function since resualt is a stringIO
        # which renpy cant pickle, so if it is returned it will be i global scope and renpy will try to pickle it
        return (resualt.getcode(), resualt.read())
    
    def put_request(url):
        opener = urllib2.build_opener(urllib2.HTTPHandler)
        req = urllib2.Request(url)
        req.add_header('Content-Type', 'application/json')
        req.add_header('Authorization', 'Basic ')
        req.get_method = lambda: 'PUT'
        opener.open(req)
     
    def delete_request(url):
        opener = urllib2.build_opener(urllib2.HTTPHandler)
        req = urllib2.Request(url)
        req.add_header('Content-Type', 'application/json')
        req.add_header('Authorization', 'Basic ')
        req.get_method = lambda: 'DELETE'
        opener.open(req)