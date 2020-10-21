# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: config/netcmn.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='config/netcmn.proto',
  package='org.lfedge.eve.config',
  syntax='proto3',
  serialized_options=b'\n\025org.lfedge.eve.configZ$github.com/lf-edge/eve/api/go/config',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13\x63onfig/netcmn.proto\x12\x15org.lfedge.eve.config\"%\n\x07ipRange\x12\r\n\x05start\x18\x01 \x01(\t\x12\x0b\n\x03\x65nd\x18\x02 \x01(\t\"]\n\x0bProxyServer\x12\x30\n\x05proto\x18\x01 \x01(\x0e\x32!.org.lfedge.eve.config.proxyProto\x12\x0e\n\x06server\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\r\"\xb2\x01\n\x0bProxyConfig\x12\x1a\n\x12networkProxyEnable\x18\x01 \x01(\x08\x12\x33\n\x07proxies\x18\x02 \x03(\x0b\x32\".org.lfedge.eve.config.ProxyServer\x12\x12\n\nexceptions\x18\x03 \x01(\t\x12\x0f\n\x07pacfile\x18\x04 \x01(\t\x12\x17\n\x0fnetworkProxyURL\x18\x05 \x01(\t\x12\x14\n\x0cproxyCertPEM\x18\x06 \x03(\x0c\"*\n\tZedServer\x12\x10\n\x08HostName\x18\x01 \x01(\t\x12\x0b\n\x03\x45ID\x18\x02 \x03(\t\"7\n\x12ZnetStaticDNSEntry\x12\x10\n\x08HostName\x18\x01 \x01(\t\x12\x0f\n\x07\x41\x64\x64ress\x18\x02 \x03(\t\"\xb5\x01\n\x06ipspec\x12-\n\x04\x64hcp\x18\x02 \x01(\x0e\x32\x1f.org.lfedge.eve.config.DHCPType\x12\x0e\n\x06subnet\x18\x03 \x01(\t\x12\x0f\n\x07gateway\x18\x05 \x01(\t\x12\x0e\n\x06\x64omain\x18\x06 \x01(\t\x12\x0b\n\x03ntp\x18\x07 \x01(\t\x12\x0b\n\x03\x64ns\x18\x08 \x03(\t\x12\x31\n\tdhcpRange\x18\t \x01(\x0b\x32\x1e.org.lfedge.eve.config.ipRange*_\n\nproxyProto\x12\x0e\n\nPROXY_HTTP\x10\x00\x12\x0f\n\x0bPROXY_HTTPS\x10\x01\x12\x0f\n\x0bPROXY_SOCKS\x10\x02\x12\r\n\tPROXY_FTP\x10\x03\x12\x10\n\x0bPROXY_OTHER\x10\xff\x01*>\n\x08\x44HCPType\x12\x0c\n\x08\x44HCPNoop\x10\x00\x12\n\n\x06Static\x10\x01\x12\x0c\n\x08\x44HCPNone\x10\x02\x12\n\n\x06\x43lient\x10\x04*]\n\x0bNetworkType\x12\x13\n\x0fNETWORKTYPENOOP\x10\x00\x12\x06\n\x02V4\x10\x04\x12\x06\n\x02V6\x10\x06\x12\x0c\n\x08\x43ryptoV4\x10\x18\x12\x0c\n\x08\x43ryptoV6\x10\x1a\x12\r\n\tCryptoEID\x10\x0e*4\n\x0cWirelessType\x12\x0c\n\x08TypeNOOP\x10\x00\x12\x08\n\x04WiFi\x10\x01\x12\x0c\n\x08\x43\x65llular\x10\x02*7\n\rWiFiKeyScheme\x12\x0e\n\nSchemeNOOP\x10\x00\x12\n\n\x06WPAPSK\x10\x01\x12\n\n\x06WPAEAP\x10\x02\x42=\n\x15org.lfedge.eve.configZ$github.com/lf-edge/eve/api/go/configb\x06proto3'
)

_PROXYPROTO = _descriptor.EnumDescriptor(
  name='proxyProto',
  full_name='org.lfedge.eve.config.proxyProto',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PROXY_HTTP', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PROXY_HTTPS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PROXY_SOCKS', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PROXY_FTP', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PROXY_OTHER', index=4, number=255,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=646,
  serialized_end=741,
)
_sym_db.RegisterEnumDescriptor(_PROXYPROTO)

proxyProto = enum_type_wrapper.EnumTypeWrapper(_PROXYPROTO)
_DHCPTYPE = _descriptor.EnumDescriptor(
  name='DHCPType',
  full_name='org.lfedge.eve.config.DHCPType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DHCPNoop', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Static', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DHCPNone', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Client', index=3, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=743,
  serialized_end=805,
)
_sym_db.RegisterEnumDescriptor(_DHCPTYPE)

DHCPType = enum_type_wrapper.EnumTypeWrapper(_DHCPTYPE)
_NETWORKTYPE = _descriptor.EnumDescriptor(
  name='NetworkType',
  full_name='org.lfedge.eve.config.NetworkType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NETWORKTYPENOOP', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='V4', index=1, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='V6', index=2, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CryptoV4', index=3, number=24,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CryptoV6', index=4, number=26,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CryptoEID', index=5, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=807,
  serialized_end=900,
)
_sym_db.RegisterEnumDescriptor(_NETWORKTYPE)

NetworkType = enum_type_wrapper.EnumTypeWrapper(_NETWORKTYPE)
_WIRELESSTYPE = _descriptor.EnumDescriptor(
  name='WirelessType',
  full_name='org.lfedge.eve.config.WirelessType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TypeNOOP', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WiFi', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Cellular', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=902,
  serialized_end=954,
)
_sym_db.RegisterEnumDescriptor(_WIRELESSTYPE)

WirelessType = enum_type_wrapper.EnumTypeWrapper(_WIRELESSTYPE)
_WIFIKEYSCHEME = _descriptor.EnumDescriptor(
  name='WiFiKeyScheme',
  full_name='org.lfedge.eve.config.WiFiKeyScheme',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SchemeNOOP', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WPAPSK', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WPAEAP', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=956,
  serialized_end=1011,
)
_sym_db.RegisterEnumDescriptor(_WIFIKEYSCHEME)

WiFiKeyScheme = enum_type_wrapper.EnumTypeWrapper(_WIFIKEYSCHEME)
PROXY_HTTP = 0
PROXY_HTTPS = 1
PROXY_SOCKS = 2
PROXY_FTP = 3
PROXY_OTHER = 255
DHCPNoop = 0
Static = 1
DHCPNone = 2
Client = 4
NETWORKTYPENOOP = 0
V4 = 4
V6 = 6
CryptoV4 = 24
CryptoV6 = 26
CryptoEID = 14
TypeNOOP = 0
WiFi = 1
Cellular = 2
SchemeNOOP = 0
WPAPSK = 1
WPAEAP = 2



_IPRANGE = _descriptor.Descriptor(
  name='ipRange',
  full_name='org.lfedge.eve.config.ipRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='org.lfedge.eve.config.ipRange.start', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end', full_name='org.lfedge.eve.config.ipRange.end', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=83,
)


_PROXYSERVER = _descriptor.Descriptor(
  name='ProxyServer',
  full_name='org.lfedge.eve.config.ProxyServer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='proto', full_name='org.lfedge.eve.config.ProxyServer.proto', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='server', full_name='org.lfedge.eve.config.ProxyServer.server', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='org.lfedge.eve.config.ProxyServer.port', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=85,
  serialized_end=178,
)


_PROXYCONFIG = _descriptor.Descriptor(
  name='ProxyConfig',
  full_name='org.lfedge.eve.config.ProxyConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='networkProxyEnable', full_name='org.lfedge.eve.config.ProxyConfig.networkProxyEnable', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='proxies', full_name='org.lfedge.eve.config.ProxyConfig.proxies', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exceptions', full_name='org.lfedge.eve.config.ProxyConfig.exceptions', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pacfile', full_name='org.lfedge.eve.config.ProxyConfig.pacfile', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='networkProxyURL', full_name='org.lfedge.eve.config.ProxyConfig.networkProxyURL', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='proxyCertPEM', full_name='org.lfedge.eve.config.ProxyConfig.proxyCertPEM', index=5,
      number=6, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=181,
  serialized_end=359,
)


_ZEDSERVER = _descriptor.Descriptor(
  name='ZedServer',
  full_name='org.lfedge.eve.config.ZedServer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='HostName', full_name='org.lfedge.eve.config.ZedServer.HostName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='EID', full_name='org.lfedge.eve.config.ZedServer.EID', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=361,
  serialized_end=403,
)


_ZNETSTATICDNSENTRY = _descriptor.Descriptor(
  name='ZnetStaticDNSEntry',
  full_name='org.lfedge.eve.config.ZnetStaticDNSEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='HostName', full_name='org.lfedge.eve.config.ZnetStaticDNSEntry.HostName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Address', full_name='org.lfedge.eve.config.ZnetStaticDNSEntry.Address', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=405,
  serialized_end=460,
)


_IPSPEC = _descriptor.Descriptor(
  name='ipspec',
  full_name='org.lfedge.eve.config.ipspec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dhcp', full_name='org.lfedge.eve.config.ipspec.dhcp', index=0,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subnet', full_name='org.lfedge.eve.config.ipspec.subnet', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gateway', full_name='org.lfedge.eve.config.ipspec.gateway', index=2,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain', full_name='org.lfedge.eve.config.ipspec.domain', index=3,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ntp', full_name='org.lfedge.eve.config.ipspec.ntp', index=4,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dns', full_name='org.lfedge.eve.config.ipspec.dns', index=5,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dhcpRange', full_name='org.lfedge.eve.config.ipspec.dhcpRange', index=6,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=463,
  serialized_end=644,
)

_PROXYSERVER.fields_by_name['proto'].enum_type = _PROXYPROTO
_PROXYCONFIG.fields_by_name['proxies'].message_type = _PROXYSERVER
_IPSPEC.fields_by_name['dhcp'].enum_type = _DHCPTYPE
_IPSPEC.fields_by_name['dhcpRange'].message_type = _IPRANGE
DESCRIPTOR.message_types_by_name['ipRange'] = _IPRANGE
DESCRIPTOR.message_types_by_name['ProxyServer'] = _PROXYSERVER
DESCRIPTOR.message_types_by_name['ProxyConfig'] = _PROXYCONFIG
DESCRIPTOR.message_types_by_name['ZedServer'] = _ZEDSERVER
DESCRIPTOR.message_types_by_name['ZnetStaticDNSEntry'] = _ZNETSTATICDNSENTRY
DESCRIPTOR.message_types_by_name['ipspec'] = _IPSPEC
DESCRIPTOR.enum_types_by_name['proxyProto'] = _PROXYPROTO
DESCRIPTOR.enum_types_by_name['DHCPType'] = _DHCPTYPE
DESCRIPTOR.enum_types_by_name['NetworkType'] = _NETWORKTYPE
DESCRIPTOR.enum_types_by_name['WirelessType'] = _WIRELESSTYPE
DESCRIPTOR.enum_types_by_name['WiFiKeyScheme'] = _WIFIKEYSCHEME
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ipRange = _reflection.GeneratedProtocolMessageType('ipRange', (_message.Message,), {
  'DESCRIPTOR' : _IPRANGE,
  '__module__' : 'config.netcmn_pb2'
  # @@protoc_insertion_point(class_scope:org.lfedge.eve.config.ipRange)
  })
_sym_db.RegisterMessage(ipRange)

ProxyServer = _reflection.GeneratedProtocolMessageType('ProxyServer', (_message.Message,), {
  'DESCRIPTOR' : _PROXYSERVER,
  '__module__' : 'config.netcmn_pb2'
  # @@protoc_insertion_point(class_scope:org.lfedge.eve.config.ProxyServer)
  })
_sym_db.RegisterMessage(ProxyServer)

ProxyConfig = _reflection.GeneratedProtocolMessageType('ProxyConfig', (_message.Message,), {
  'DESCRIPTOR' : _PROXYCONFIG,
  '__module__' : 'config.netcmn_pb2'
  # @@protoc_insertion_point(class_scope:org.lfedge.eve.config.ProxyConfig)
  })
_sym_db.RegisterMessage(ProxyConfig)

ZedServer = _reflection.GeneratedProtocolMessageType('ZedServer', (_message.Message,), {
  'DESCRIPTOR' : _ZEDSERVER,
  '__module__' : 'config.netcmn_pb2'
  # @@protoc_insertion_point(class_scope:org.lfedge.eve.config.ZedServer)
  })
_sym_db.RegisterMessage(ZedServer)

ZnetStaticDNSEntry = _reflection.GeneratedProtocolMessageType('ZnetStaticDNSEntry', (_message.Message,), {
  'DESCRIPTOR' : _ZNETSTATICDNSENTRY,
  '__module__' : 'config.netcmn_pb2'
  # @@protoc_insertion_point(class_scope:org.lfedge.eve.config.ZnetStaticDNSEntry)
  })
_sym_db.RegisterMessage(ZnetStaticDNSEntry)

ipspec = _reflection.GeneratedProtocolMessageType('ipspec', (_message.Message,), {
  'DESCRIPTOR' : _IPSPEC,
  '__module__' : 'config.netcmn_pb2'
  # @@protoc_insertion_point(class_scope:org.lfedge.eve.config.ipspec)
  })
_sym_db.RegisterMessage(ipspec)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
