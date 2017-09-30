from peewee import *

database = MySQLDatabase('userservice', **{'host': '10.11.12.186', 'password': 'Konka123!@#', 'user': 'cssroot'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Appinfo(BaseModel):
    app_launch_count = IntegerField(null=True)
    app_name = CharField(null=True)
    app_pkg_name = CharField(null=True)
    app_version = CharField(null=True)
    appinfo = BigIntegerField(db_column='appinfo_id')
    createtime = DateTimeField(db_column='createTime')
    imei = CharField(index=True, null=True)

    class Meta:
        db_table = 'appinfo'
        indexes = (
            (('appinfo', 'createtime'), True),
        )
        primary_key = CompositeKey('appinfo', 'createtime')

class Appinfo201605(BaseModel):
    app_launch_count = IntegerField(null=True)
    app_name = CharField(null=True)
    app_pkg_name = CharField(null=True)
    app_version = CharField(null=True)
    appinfo = BigIntegerField(db_column='appinfo_id', primary_key=True)
    createtime = DateTimeField(db_column='createTime', null=True)
    imei = CharField(null=True)

    class Meta:
        db_table = 'appinfo_201605'

class Appinstall(BaseModel):
    app_name = CharField(null=True)
    app_pkg_name = CharField(null=True)
    createtime = DateTimeField(db_column='createTime')
    imei = CharField()
    installid = BigIntegerField()
    operate_time = CharField(null=True)
    operate_type = CharField()

    class Meta:
        db_table = 'appinstall'
        indexes = (
            (('installid', 'createtime'), True),
        )
        primary_key = CompositeKey('createtime', 'installid')

class Baseinfo(BaseModel):
    baseinfo = BigIntegerField(db_column='baseinfo_id', primary_key=True)
    brand = CharField(null=True)
    createtime = DateTimeField(db_column='createTime', null=True)
    device_model = CharField(null=True)
    imei = CharField(null=True, unique=True)
    phone_hardware_version = CharField(null=True)
    updatetime = DateTimeField(db_column='updateTime', null=True)

    class Meta:
        db_table = 'baseinfo'

class Chargeinfo(BaseModel):
    createtime = DateTimeField(null=True)
    endlevel = CharField(null=True)
    endtime = DateTimeField(null=True)
    id = BigIntegerField(primary_key=True)
    imei = CharField(null=True)
    startlevel = CharField(null=True)
    starttime = DateTimeField(null=True)

    class Meta:
        db_table = 'chargeinfo'

class Country(BaseModel):
    chinesename = CharField(db_column='chineseName', null=True)
    countryid = BigIntegerField(db_column='countryId', primary_key=True)
    fullname = CharField(db_column='fullName', null=True)
    shortname = CharField(db_column='shortName', null=True)

    class Meta:
        db_table = 'country'

class Elecimage(BaseModel):
    createby = CharField(db_column='createBy', null=True)
    createtime = DateTimeField(db_column='createTime', null=True)
    i = BigIntegerField(db_column='i_id', primary_key=True)
    imageurl = TextField(db_column='imageUrl', null=True)
    updateby = CharField(db_column='updateBy', null=True)
    updatetime = DateTimeField(db_column='updateTime', null=True)

    class Meta:
        db_table = 'elecimage'

class Elecimageover(BaseModel):
    areaid = BigIntegerField(null=True)
    createby = CharField(db_column='createBy', null=True)
    createtime = DateTimeField(db_column='createTime', null=True)
    i = BigIntegerField(db_column='i_id', primary_key=True)
    imageurl = TextField(db_column='imageUrl', null=True)
    updateby = CharField(db_column='updateBy', null=True)
    updatetime = DateTimeField(db_column='updateTime', null=True)

    class Meta:
        db_table = 'elecimageover'

class Electroniccard(BaseModel):
    card = BigIntegerField(db_column='card_id', primary_key=True)
    city = CharField(null=True)
    createtime = DateTimeField(db_column='createTime', null=True)
    iid = CharField(null=True)
    imei = CharField(null=True, unique=True)
    locationinfo = CharField(db_column='locationInfo', null=True)
    phonenumber = CharField(db_column='phoneNumber', null=True)
    province = CharField(null=True)
    repairstate = CharField(db_column='repairState', null=True)
    replacedate = IntegerField(db_column='replaceDate', null=True)
    smscenternumber = CharField(db_column='smsCenterNumber', null=True)
    softwareversion = CharField(db_column='softwareVersion', null=True)
    uptype = IntegerField(db_column='upType', null=True)
    updatetime = DateTimeField(db_column='updateTime', null=True)
    warrantydate = IntegerField(db_column='warrantyDate', null=True)

    class Meta:
        db_table = 'electroniccard'

class Electroniccardover(BaseModel):
    country = CharField(null=True)
    createtime = DateTimeField(db_column='createTime', null=True)
    detail = TextField(null=True)
    flash = CharField(null=True)
    imei = CharField(null=True, unique=True)
    lcm = CharField(null=True)
    location = CharField(null=True)
    maincamera = CharField(db_column='mainCamera', null=True)
    overid = BigIntegerField(primary_key=True)
    phonemodel = CharField(db_column='phoneModel', null=True)
    platformmodel = CharField(db_column='platformModel', null=True)
    replacedate = IntegerField(db_column='replaceDate', null=True)
    softwareversion = CharField(db_column='softwareVersion', null=True)
    subcamera = CharField(db_column='subCamera', null=True)
    totalram = CharField(db_column='totalRam', null=True)
    totalrom = CharField(db_column='totalRom', null=True)
    updatetime = DateTimeField(db_column='updateTime', null=True)
    warrantydate = IntegerField(db_column='warrantyDate', null=True)

    class Meta:
        db_table = 'electroniccardover'

class Loginfo(BaseModel):
    createtime = DateTimeField(db_column='createTime', null=True)
    exceptiontype = CharField(null=True)
    fileurl = CharField(null=True)
    imei = CharField()
    logid = BigIntegerField(primary_key=True)
    model = CharField(null=True)
    pkgname = CharField(null=True)

    class Meta:
        db_table = 'loginfo'

class Mcccode(BaseModel):
    country = CharField(null=True)
    country_en = CharField(null=True)
    internalcode = BigIntegerField(null=True)
    iso = CharField(null=True)
    mcc = BigIntegerField(null=True)

    class Meta:
        db_table = 'mcccode'
        primary_key = False

class OdmOwn(BaseModel):
    odmversion = CharField(null=True)
    ooid = PrimaryKeyField()
    ownversion = CharField(null=True)

    class Meta:
        db_table = 'odm_own'

class Odmcard(BaseModel):
    country = CharField(null=True)
    createtime = DateTimeField(db_column='createTime', null=True)
    detail = TextField(null=True)
    flash = CharField(null=True)
    imei = CharField(null=True, unique=True)
    lcm = CharField(null=True)
    location = CharField(null=True)
    maincamera = CharField(db_column='mainCamera', null=True)
    odmid = BigIntegerField(primary_key=True)
    phonemodel = CharField(db_column='phoneModel', null=True)
    platformmodel = CharField(db_column='platformModel', null=True)
    replacedate = IntegerField(db_column='replaceDate', null=True)
    softwareversion = CharField(db_column='softwareVersion', null=True)
    subcamera = CharField(db_column='subCamera', null=True)
    totalram = CharField(db_column='totalRam', null=True)
    totalrom = CharField(db_column='totalRom', null=True)
    updatetime = DateTimeField(db_column='updateTime', null=True)
    warrantydate = IntegerField(db_column='warrantyDate', null=True)

    class Meta:
        db_table = 'odmcard'

class OdmcardCopy(BaseModel):
    country = CharField(null=True)
    createtime = DateTimeField(db_column='createTime', null=True)
    detail = TextField(null=True)
    flash = CharField(null=True)
    imei = CharField(null=True, unique=True)
    lcm = CharField(null=True)
    location = CharField(null=True)
    maincamera = CharField(db_column='mainCamera', null=True)
    odmid = BigIntegerField(primary_key=True)
    phonemodel = CharField(db_column='phoneModel', null=True)
    platformmodel = CharField(db_column='platformModel', null=True)
    replacedate = IntegerField(db_column='replaceDate', null=True)
    softwareversion = CharField(db_column='softwareVersion', null=True)
    subcamera = CharField(db_column='subCamera', null=True)
    totalram = CharField(db_column='totalRam', null=True)
    totalrom = CharField(db_column='totalRom', null=True)
    updatetime = DateTimeField(db_column='updateTime', null=True)
    warrantydate = IntegerField(db_column='warrantyDate', null=True)

    class Meta:
        db_table = 'odmcard_copy'

class Repairrecord(BaseModel):
    barcode = CharField(null=True)
    cid = IntegerField(null=True)
    city = CharField(null=True)
    imei = CharField(null=True)
    lac = IntegerField(null=True)
    mcc = IntegerField(null=True)
    mnc = IntegerField(null=True)
    province = CharField(null=True)
    r = BigIntegerField(db_column='r_id', primary_key=True)
    repairdate = DateTimeField(null=True)
    type = IntegerField()
    wifilist = TextField(null=True)

    class Meta:
        db_table = 'repairrecord'

class Servicephone(BaseModel):
    active = CharField(null=True)
    areaid = BigIntegerField(db_column='areaId', null=True)
    createby = CharField(db_column='createBy', null=True)
    createtime = DateTimeField(db_column='createTime', null=True)
    phoneid = BigIntegerField(db_column='phoneId', primary_key=True)
    phonenum = CharField(db_column='phoneNum')
    updateby = CharField(db_column='updateBy', null=True)
    updatetime = DateTimeField(db_column='updateTime', null=True)

    class Meta:
        db_table = 'servicephone'

class Softwareversion(BaseModel):
    createtime = DateTimeField(db_column='createTime', null=True)
    imei = CharField(null=True)
    phone_software_version = CharField(null=True)
    softversion = BigIntegerField(db_column='softversion_id', primary_key=True)
    update_info = CharField(null=True)

    class Meta:
        db_table = 'softwareversion'

class SysDictionary(BaseModel):
    code = CharField()
    dictionarytype = IntegerField(db_column='dictionarytype_id')
    isdefault = IntegerField()
    seq = IntegerField()
    state = IntegerField()
    text = CharField()

    class Meta:
        db_table = 'sys_dictionary'

class SysDictionarytype(BaseModel):
    code = CharField()
    description = CharField(null=True)
    name = CharField()
    pid = IntegerField(null=True)
    seq = IntegerField()

    class Meta:
        db_table = 'sys_dictionarytype'

class SysOrganization(BaseModel):
    address = CharField(null=True)
    code = CharField()
    createdatetime = DateTimeField()
    icon = CharField(null=True)
    name = CharField()
    pid = IntegerField(null=True)
    seq = IntegerField()

    class Meta:
        db_table = 'sys_organization'

class SysResource(BaseModel):
    createdatetime = DateTimeField()
    description = CharField(null=True)
    icon = CharField(null=True)
    name = CharField()
    pid = IntegerField(null=True)
    resourcetype = IntegerField()
    seq = IntegerField()
    state = IntegerField()
    url = CharField(null=True)

    class Meta:
        db_table = 'sys_resource'

class SysRole(BaseModel):
    description = CharField(null=True)
    isdefault = IntegerField()
    name = CharField()
    seq = IntegerField()

    class Meta:
        db_table = 'sys_role'

class SysRoleResource(BaseModel):
    resource = IntegerField(db_column='resource_id')
    role = IntegerField(db_column='role_id')

    class Meta:
        db_table = 'sys_role_resource'
        indexes = (
            (('role', 'resource'), True),
        )
        primary_key = CompositeKey('resource', 'role')

class SysUser(BaseModel):
    age = IntegerField()
    createdatetime = DateTimeField()
    isdefault = IntegerField()
    loginname = CharField(unique=True)
    name = CharField()
    organization = IntegerField(db_column='organization_id')
    password = CharField()
    sex = IntegerField()
    state = IntegerField()
    usertype = IntegerField()

    class Meta:
        db_table = 'sys_user'

class SysUserRole(BaseModel):
    role = IntegerField(db_column='role_id')
    user = IntegerField(db_column='user_id')

    class Meta:
        db_table = 'sys_user_role'
        indexes = (
            (('user', 'role'), True),
        )
        primary_key = CompositeKey('role', 'user')

class Userfeedback(BaseModel):
    createtime = DateTimeField(db_column='createTime', null=True)
    imei = CharField(null=True)
    phonenumber = CharField(db_column='phoneNumber', null=True)
    problemdescription = TextField(db_column='problemDescription', null=True)
    problemtype = CharField(db_column='problemType', null=True)
    screenshot1 = TextField(null=True)
    screenshot2 = TextField(null=True)
    screenshot3 = TextField(null=True)
    softwareversion = CharField(db_column='softwareVersion', null=True)
    userfeedback = BigIntegerField(db_column='userFeedback_id', primary_key=True)

    class Meta:
        db_table = 'userfeedback'

class Warrantydate(BaseModel):
    createdate = DateTimeField(db_column='createDate', null=True)
    replacedate = IntegerField(db_column='replaceDate', null=True)
    warrantydate = IntegerField(db_column='warrantyDate', null=True)
    wid = PrimaryKeyField()

    class Meta:
        db_table = 'warrantydate'

class Website(BaseModel):
    address = CharField(null=True)
    buildtime = CharField(db_column='buildTime')
    city = CharField(null=True)
    createby = CharField(db_column='createBy', null=True)
    createtime = DateTimeField(db_column='createTime', null=True)
    email = CharField(null=True)
    fax = CharField(null=True)
    flag = CharField(null=True)
    manager = CharField(null=True)
    postalcode = CharField(db_column='postalCode', null=True)
    principal = CharField(null=True)
    province = CharField(null=True)
    site = CharField(null=True)
    siteattr = CharField(db_column='siteAttr', null=True)
    specialtype = CharField(db_column='specialType', null=True)
    supersite = CharField(db_column='superSite', null=True)
    telephone = CharField(null=True)
    updateby = CharField(db_column='updateBy', null=True)
    updatetime = DateTimeField(db_column='updateTime', null=True)
    w = BigIntegerField(db_column='w_id', primary_key=True)

    class Meta:
        db_table = 'website'

class Websiteover(BaseModel):
    address = CharField(null=True)
    areaid = BigIntegerField(null=True)
    buildtime = CharField(db_column='buildTime')
    city = CharField(null=True)
    createby = CharField(db_column='createBy', null=True)
    createtime = DateTimeField(db_column='createTime', null=True)
    email = CharField(null=True)
    fax = CharField(null=True)
    flag = CharField(null=True)
    manager = CharField(null=True)
    postalcode = CharField(db_column='postalCode', null=True)
    principal = CharField(null=True)
    province = CharField(null=True)
    site = CharField(null=True)
    siteattr = CharField(db_column='siteAttr', null=True)
    specialtype = CharField(db_column='specialType', null=True)
    supersite = CharField(db_column='superSite', null=True)
    telephone = CharField(null=True)
    updateby = CharField(db_column='updateBy', null=True)
    updatetime = DateTimeField(db_column='updateTime', null=True)
    w = BigIntegerField(db_column='w_id', primary_key=True)

    class Meta:
        db_table = 'websiteover'

