--- yt_dlp/networking/_curlcffi.py.orig	2026-03-17 23:25:33 UTC
+++ yt_dlp/networking/_curlcffi.py
@@ -33,7 +33,7 @@ curl_cffi_version = tuple(map(int, re.split(r'[^\d]+',
 
 curl_cffi_version = tuple(map(int, re.split(r'[^\d]+', curl_cffi.__version__)[:3]))
 
-if curl_cffi_version != (0, 5, 10) and not (0, 10) <= curl_cffi_version < (0, 15):
+if curl_cffi_version != (0, 5, 10) and not (0, 10) <= curl_cffi_version < (0, 16):
     curl_cffi._yt_dlp__version = f'{curl_cffi.__version__} (unsupported)'
     raise ImportError('Only curl_cffi versions 0.5.10 and 0.10.x through 0.14.x are supported')
 
