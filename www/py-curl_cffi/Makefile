PORTNAME=	curl_cffi
PORTVERSION=	0.14.0
DISTVERSIONPREFIX=	v
CATEGORIES=	 www python
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	y@trombik.org
COMMENT=	Python binding for curl-impersonate fork via cffi
WWW=		https://github.com/lexiforest/curl_cffi

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

BUILD_DEPENDS=	\
	bash:shells/bash \
	${PYTHON_PKGNAMEPREFIX}cffi>=0:devel/py-cffi@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}certifi>0:security/py-certifi@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}wheel>=0:devel/py-wheel@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}setuptools>0:devel/py-setuptools@${PY_FLAVOR}

LIB_DEPENDS=	\
	libcurl.so:ftp/curl \
	libcurl-impersonate.so:www/curl-impersonate

USES=		python gmake autoreconf:build libtool:build
USE_PYTHON=	autoplist pep517
USE_GITHUB=	yes
GH_ACCOUNT=	lexiforest

ALL_TARGET=	build
MAKE_ARGS=	V=1
CFLAGS+=	-I${LOCALBASE}/include
LDFLAGS+=	-L${LOCALBASE}/lib -lcurl-impersonate -Wl,-rpath=${LOCALBASE}/lib

DO_MAKE_BUILD=	${SETENVI} ${WRK_ENV} ${MAKE_ENV} ${MAKE_CMD} ${MAKE_FLAGS} \
				${MAKEFILE} ${_MAKE_JOBS} ${MAKE_ARGS:N${DESTDIRNAME}=*}

GH_TUPLE=	\
	curl:curl:curl-${CURL_CFFI_CURL_VERSION}:curl \
	lexiforest:curl-impersonate:v${CURL_CFFI_LIBCURL_IMPERSONATE_VERSION}:curl_impersonate

# see Makefile
CURL_CFFI_LIBCURL_IMPERSONATE_VERSION=	1.2.5
CURL_CFFI_CURL_VERSION=	8_15_0

post-extract:
.for _org _project _tag _src_group in ${GH_TUPLE:C/:/ /g}
.	if ${_project} == curl
		(cd ${WRKSRC} && ${LN} -s ${WRKDIR}/curl-curl-${CURL_CFFI_CURL_VERSION} curl-${CURL_CFFI_CURL_VERSION})
.	elif ${_project} == curl-impersonate
		${MKDIR} ${WRKSRC}/curl-impersonate-${CURL_CFFI_LIBCURL_IMPERSONATE_VERSION}
		(cd ${WRKSRC}/curl-impersonate-${CURL_CFFI_LIBCURL_IMPERSONATE_VERSION} && \
			${LN} -s ${WRKDIR}/${_project}-${_tag:C/v//}/patches .)
.	endif
.endfor

pre-configure:
	@${REINPLACE_CMD} -e 's|%%LOCALBASE%%|${LOCALBASE}|' ${WRKSRC}/libs.json

pre-build:
	@(cd ${BUILD_WRKSRC}; if ! ${DO_MAKE_BUILD} ${ALL_TARGET}; then \
		if [ -n "${BUILD_FAIL_MESSAGE}" ] ; then \
			${ECHO_MSG} "===> Compilation failed unexpectedly."; \
			(${ECHO_CMD} "${BUILD_FAIL_MESSAGE}") | ${FMT_80} ; \
			fi; \
		${FALSE}; \
		fi)

.include <bsd.port.mk>
