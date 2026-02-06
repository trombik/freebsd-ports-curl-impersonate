PORTNAME=	curl-impersonate
PORTVERSION=	1.4.3
DISTVERSIONPREFIX=	v
CATEGORIES=	www

MAINTAINER=	y@trombik.org
COMMENT=	An active fork of curl-impersonate with more versions and build targets
WWW=		https://github.com/lexiforest/curl-impersonate/

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

EXTRACT_DEPENDS= zip:archivers/zip

BUILD_DEPENDS=	\
	bash:shells/bash \
	unzip:archivers/unzip

USES=	libtool pkgconfig autoreconf:build gmake cmake:indirect ninja:build
USE_GITHUB=	yes
GH_ACCOUNT=	lexiforest
GH_TUPLE=	\
	curl:curl:curl-${CURL_IM_CURL_VERSION}:curl \
	facebook:zstd:v${CURL_IM_ZSTD_VERSION}:zstd \
	google:boringssl:${CURL_IM_BORING_SSL_VERSION}:boringssl \
	google:brotli:v${CURL_IM_BROTLI_VERSION}:brotli	\
	madler:zlib:v${CURL_IM_ZLIB_VERSION}:zlib \
	nghttp2:nghttp2:v${CURL_IM_NGHTTP2_VERSION}:nghttp2	\
	ngtcp2:nghttp3:v${CURL_IM_NGHTTP3_VERSION}:nghttp3 \
	ngtcp2:ngtcp2:v${CURL_IM_NGTCP2_VERSION}:ngtcp2	\
	ngtcp2:sfparse:${CURL_IM_NGHTTP2_SFPARS_VERSION}:sfparse \


GNU_CONFIGURE=	yes

ALL_TARGET=	build
MAKE_ARGS=	V=1 SUBJOBS=${MAKE_JOBS_NUMBER}
CFLAGS+=	-fPIC  -Werror=implicit-function-declaration
LDFLAGS+=	-L${LOCALBASE}/lib --verbose

# see Makefile.in
CURL_IM_BORING_SSL_VERSION=	673e61fc215b178a90c0e67858bbf162c8158993
CURL_IM_BROTLI_VERSION=	1.2.0
CURL_IM_CURL_VERSION=	8_15_0
CURL_IM_LIBIDN2_VERSION=	2.3.7
CURL_IM_LIBUNISTRING_VERSION=	1.1
CURL_IM_NGHTTP2_VERSION=	1.63.0
CURL_IM_NGHTTP3_VERSION=	1.9.0
CURL_IM_NGTCP2_VERSION=	1.11.0
CURL_IM_ZLIB_VERSION=	1.3.1
CURL_IM_ZSTD_VERSION=	1.5.6

# libunistring and libidn2 on GNU FTP sites
MASTER_SITES+=	\
	https://ftpmirror.gnu.org/gnu/libunistring/:libunistring \
	https://ftpmirror.gnu.org/gnu/libidn/:libidn2

DISTFILES+=	\
	libunistring-${CURL_IM_LIBUNISTRING_VERSION}.tar.gz:libunistring \
	libidn2-${CURL_IM_LIBIDN2_VERSION}.tar.gz:libidn2

# git submodule for nghttp3
CURL_IM_NGHTTP2_SFPARS_VERSION=	7eaf5b6

post-extract:
	(cd ${WRKDIR}/libidn2-${CURL_IM_LIBIDN2_VERSION} && ${PATCH} < ${FILESDIR}/libidn2.patch)
	${RM} -r ${WRKDIR}/nghttp3-${CURL_IM_NGHTTP3_VERSION}/lib/sfparse
	${CP} -r ${WRKDIR}/sfparse-${CURL_IM_NGHTTP2_SFPARS_VERSION} ${WRKDIR}/nghttp3-${CURL_IM_NGHTTP3_VERSION}/lib/sfparse
	(cd ${WRKSRC} && ${TAR} -czf libidn2-${CURL_IM_LIBIDN2_VERSION}.tar.gz -C ${WRKDIR} libidn2-${CURL_IM_LIBIDN2_VERSION})
	(cd ${WRKSRC} && ${TAR} -czf libunistring-${CURL_IM_LIBUNISTRING_VERSION}.tar.gz -C ${WRKDIR} libunistring-${CURL_IM_LIBUNISTRING_VERSION})
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

post-install:
	# resolve conflict with ftp/curl
	${MV} ${STAGEDIR}${PREFIX}/bin/wcurl ${STAGEDIR}${PREFIX}/bin/wcurl-impersonate

.include <bsd.port.mk>
