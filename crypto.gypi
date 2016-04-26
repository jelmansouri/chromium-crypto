# Copyright 2014 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'variables': {
    # Put all transitive dependencies for Windows HMAC here.
    # This is required so that we can build them for nacl win64.
    'variables': {
      'hmac_win64_related_sources': [
        'hmac.cc',
        'hmac.h',
        'hmac_win.cc',
        'secure_util.cc',
        'secure_util.h',
        'symmetric_key.h',
        'symmetric_key_win.cc',
        'third_party/nss/chromium-prtypes.h',
        'third_party/nss/chromium-sha256.h',
        'third_party/nss/sha512.cc',
        'wincrypt_shim.h',
      ],
    },
    'crypto_sources': [
      # NOTE: all transitive dependencies of HMAC on windows need
      #     to be placed in the source list above.
      '<@(hmac_win64_related_sources)',
      'aead.cc',
      'aead.h',
      'apple_keychain.h',
      'apple_keychain_ios.mm',
      'apple_keychain_mac.mm',
      'auto_cbb.h',
      'capi_util.cc',
      'capi_util.h',
      'crypto_export.h',
      'cssm_init.cc',
      'cssm_init.h',
      'curve25519.cc',
      'curve25519.h',
      'ec_private_key.cc',
      'ec_private_key.h',
      'ec_signature_creator.cc',
      'ec_signature_creator.h',
      'ec_signature_creator_impl.cc',
      'ec_signature_creator_impl.h',
      'encryptor.cc',
      'encryptor.h',
      'hkdf.cc',
      'hkdf.h',
      'hmac_openssl.cc',
      'mac_security_services_lock.cc',
      'mac_security_services_lock.h',
      'mock_apple_keychain.cc',
      'mock_apple_keychain.h',
      'mock_apple_keychain_ios.cc',
      'mock_apple_keychain_mac.cc',
      'p224_spake.cc',
      'p224_spake.h',
      'nss_crypto_module_delegate.h',
      'nss_key_util.cc',
      'nss_key_util.h',
      'nss_util.cc',
      'nss_util.h',
      'nss_util_internal.h',
      'openssl_bio_string.cc',
      'openssl_bio_string.h',
      'openssl_util.cc',
      'openssl_util.h',
      'p224.cc',
      'p224.h',
      'random.h',
      'random.cc',
      'rsa_private_key.cc',
      'rsa_private_key.h',
      'scoped_capi_types.h',
      'scoped_nss_types.h',
      'secure_hash.cc',
      'secure_hash.h',
      'sha2.cc',
      'sha2.h',
      'signature_creator.cc',
      'signature_creator.h',
      'signature_verifier.cc',
      'signature_verifier.h',
      'symmetric_key_openssl.cc',
    ],
    'nacl_win64_sources': [
      '<@(hmac_win64_related_sources)',
      'random.cc',
      'random.h',
    ],
  }
}
