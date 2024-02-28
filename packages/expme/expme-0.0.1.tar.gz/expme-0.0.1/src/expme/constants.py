from .util import Constant


class ServerType(Constant):
    BES = "bes"
    JBOSS = "jboss"
    JETTY = "jetty"
    RESIN = "resin"
    TOMCAT = "tomcat"
    TONGWEB = "tongweb"
    WEBLOGIC = "weblogic"
    WEBSPHERE = "websphere"

    CHOICES = (
        (BES, "BES"),
        (JBOSS, "JBoss"),
        (JETTY, "Jetty"),
        (RESIN, "Resin"),
        (TOMCAT, "Tomcat"),
        (TONGWEB, "TongWeb"),
        (WEBLOGIC, "Weblogic"),
        (WEBSPHERE, "Websphere"),
    )


class PayloadFormat(Constant):
    RAW_JAVA = "raw_java"
    RAW_JSP = "raw_jsp"
    OBFUSCATED_JSP = "obfuscated_jsp"
    RAW_JSPX = "raw_jspx"
    OBFUSCATED_JSPX = "obfuscated_jspx"
    BCEL_PAYLOAD = "bcel_payload"
    CLASS_BYTECODE = "class_bytecode"
    YSOSERIAL = "ysoserial"
    XMLDECODER_XML = "xmldecoder_xml"
    SPRING_BEAN_XML = "spring_bean_xml"
    XSTREAM_XML = "xstream_xml"

    CHOICES = (
        (RAW_JAVA, "Raw Java"),
        (RAW_JSP, "Raw JSP"),
        (OBFUSCATED_JSP, "Obfuscated JSP"),
        (RAW_JSPX, "Raw JSPX"),
        (OBFUSCATED_JSPX, "Obfuscated JSPX"),
        (BCEL_PAYLOAD, "BCEL Payload"),
        (CLASS_BYTECODE, "Class Bytecode"),
        (YSOSERIAL, "YSoSerial"),
        (XMLDECODER_XML, "XMLDecoder XML"),
        (SPRING_BEAN_XML, "Spring Bean XML"),
        (XSTREAM_XML, "XStream XML"),
    )


class YsoserialType(Constant):
    COMMONS_BEANUTILS_1_6 = "CommonsBeanutils_1_6"
    COMMONS_BEANUTILS_1_8 = "CommonsBeanutils_1_8"
    COMMONS_BEANUTILS_1_9 = "CommonsBeanutils_1_9"
    COMMONS_COLLECTIONS_3_SCRIPTENGINE = "CommonsCollections_3_ScriptEngine"
    COMMONS_COLLECTIONS_3_TEMPLATESIMPL = "CommonsCollections_3_TemplatesImpl"
    COMMONS_COLLECTIONS_4 = "CommonsCollections_4"
    FASTJSON = "FastJson"
    FINE_REPORT_10_HIBERNATE_5 = "FineReport_10_Hibernate_5"
    JDK7U21 = "Jdk7u21"
    SPRINGFASTJSON = "SpringFastjson"

    CHOICES = (
        (COMMONS_BEANUTILS_1_6, "CommonsBeanutils_1_6"),
        (COMMONS_BEANUTILS_1_8, "CommonsBeanutils_1_8"),
        (COMMONS_BEANUTILS_1_9, "CommonsBeanutils_1_9"),
        (COMMONS_COLLECTIONS_3_SCRIPTENGINE, "CommonsCollections_3_ScriptEngine"),
        (COMMONS_COLLECTIONS_3_TEMPLATESIMPL, "CommonsCollections_3_TemplatesImpl"),
        (COMMONS_COLLECTIONS_4, "CommonsCollections_4"),
        (FASTJSON, "FastJson"),
        (FINE_REPORT_10_HIBERNATE_5, "FineReport_10_Hibernate_5"),
        (JDK7U21, "Jdk7u21"),
        (SPRINGFASTJSON, "SpringFastjson"),
    )
