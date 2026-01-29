PORTNAME=	scrapy-impersonate
PORTVERSION=	1.6.2
CATEGORIES=	www python
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	y@trombik.org
COMMENT=	Scrapy download handler that impersonates browsers' TLS signatures
WWW=		https://github.com/jxlil/scrapy-impersonate

RUN_DEPENDS=	\
	${PYTHON_PKGNAMEPREFIX}scrapy>0:www/py-scrapy@${PY_FLAVOR}
LIB_DEPENDS=	\
	libcurl-impersonate.so:www/curl-impersonate

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

USES=		python
USE_PYTHON=	autoplist distutils
USE_GITHUB=	yes
GH_ACCOUNT=	jxlil

.include <bsd.port.mk>
