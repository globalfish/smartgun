Python code and associated files for the project.

NtwkCamTest.py: test code to test IP camera access using OpenCV. Just reads video stream and displays.

smartgun.py: Nerfgun demo. 
Usage: smartgun BUILTIN   (uses builtin camera, e.g. on laptop)
       smartgun PI (uses Pi camera on the Raspberry Pi)
       smartgun DLINK2312 user pass 1.2.3.4 (uses DLink DCS-2312L camera with IP address 1.2.3.4 
                and username = 'user' and password = 'pass')
       smartgun DLINK930 user pass 1.2.3.4(uses DLink DCS-930 camera with IP address 1.2.3.4 
                and username = 'user' and password = 'pass')
                
The separate cases for the two DLink cameras are due to the differing URLs for the video streams.
