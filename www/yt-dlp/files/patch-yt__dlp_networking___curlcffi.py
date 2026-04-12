--- yt_dlp/networking/_curlcffi.py.orig	2026-04-13 10:43:07 UTC
+++ yt_dlp/networking/_curlcffi.py
@@ -33,7 +33,7 @@ curl_cffi_version = tuple(map(int, re.split(r'[^\d]+',
 
 curl_cffi_version = tuple(map(int, re.split(r'[^\d]+', curl_cffi.__version__)[:3]))
 
-if curl_cffi_version != (0, 5, 10) and not (0, 10) <= curl_cffi_version < (0, 14):
+if curl_cffi_version != (0, 5, 10) and not (0, 10) <= curl_cffi_version < (0, 16):
     curl_cffi._yt_dlp__version = f'{curl_cffi.__version__} (unsupported)'
     raise ImportError('Only curl_cffi versions 0.5.10, 0.10.x, 0.11.x, 0.12.x, 0.13.x are supported')
 
