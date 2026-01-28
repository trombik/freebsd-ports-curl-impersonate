PORTNAME=	curl-impersonate
PORTVERSION=	1.3.0
DISTVERSION=	v${PORTVERSION}
CATEGORIES=	www

MAINTAINER=	y@trombik.org
COMMENT=	An active fork of curl-impersonate with more versions and build targets
WWW=		https://github.com/lexiforest/curl-impersonate/

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

EXTRACT_DEPENDS= zip:archivers/zip

BUILD_DEPENDS=	bash:shells/bash \
	unzip:archivers/unzip

LIB_DEPENDS=	libcurl.so:ftp/curl \
	libzstd.so:archivers/zstd

USES=	libtool pkgconfig autoreconf:build gmake cmake:indirect ninja:build
USE_GITHUB=	yes
GH_ACCOUNT=	lexiforest
GH_TUPLE=	\
			google:brotli:v${CURL_IM_BROTLI_VERSION}:brotli	\
			nghttp2:nghttp2:v${CURL_IM_NGHTTP2_VERSION}:nghttp2	\
			ngtcp2:nghttp3:v${CURL_IM_NGHTTP3_VERSION}:nghttp3 \
			ngtcp2:ngtcp2:v${CURL_IM_NGTCP2_VERSION}:ngtcp2	\
			c-ares:c-ares:v${CURL_IM_CARES_VERSION}:c_ares		\
			curl:curl:curl-${CURL_IM_CURL_VERSION}:curl \
			google:boringssl:${CURL_IM_BORING_SSL_VERSION}:boringssl \
			ngtcp2:sfparse:${CURL_IM_NGHTTP2_SFPARS_VERSION}:sfparse \

GNU_CONFIGURE=	yes
CONFIGURE_ARGS=	--with-zstd=${PREFIX}
ALL_TARGET=	build
MAKE_ARGS=	V=1 SUBJOBS=${MAKE_JOBS_NUMBER}

CURL_IM_BROTLI_VERSION=	1.1.0
CURL_IM_NGHTTP2_VERSION=	1.63.0
CURL_IM_NGHTTP3_VERSION=	1.9.0
CURL_IM_NGTCP2_VERSION=	1.11.0
CURL_IM_CARES_VERSION=	1.30.0
CURL_IM_CURL_VERSION=	8_15_0
CURL_IM_BORING_SSL_VERSION=	673e61fc215b178a90c0e67858bbf162c8158993

# git submodule
CURL_IM_NGHTTP2_SFPARS_VERSION=	7eaf5b6

post-extract:
.for _org _project _tag _src_group in ${GH_TUPLE:C/:/ /g}
.	if ${_project} == boringssl
		(cd ${WRKDIR} && zip -q -r ${WRKSRC}/${_project}-${_tag}.zip ${_project}-${_tag})
.	elif ${_project} == nghttp2 || ${_project} == ngtcp2 || ${_project} == nghttp3
		(cd ${WRKSRC} && ${TAR} -cyf ${_project}-${_tag:C/v//}.tar.bz2 -C ${WRKDIR} ${_project}-${_tag:C/v//})
.	elif ${_project} == curl
		(cd ${WRKSRC} && ${TAR} -czf ${_project}-${_tag:C/curl-//}.tar.gz -C ${WRKDIR} ${_project}-${_tag:C/v//})
.	else
		(cd ${WRKSRC} && ${TAR} -czf ${_project}-${_tag:C/v//}.tar.gz -C ${WRKDIR} ${_project}-${_tag:C/v//})
.	endif
.endfor

.include <bsd.port.mk>
