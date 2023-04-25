from impacket.ntlm import compute_lmhash, compute_nthash, compute_response
from impacket.ntlm import NTLMAuthChallengeResponse, NTLMAuthNegotiate

def crack_ntlmv2_hash(ntlmv2_hash, challenge, username, domain, lmhash=None):
    # Compute the LM hash and NT hash from the password
    lm_hash = lmhash.encode('utf-16le') if lmhash else compute_lmhash('')
    nt_hash = compute_nthash('')

    # Compute the NTLMv2 response from the hash and the challenge
    ntlmv2_response = compute_response(nt_hash, challenge)

    # Build the NTLMv2 authentication message
    negotiate = NTLMAuthNegotiate()
    challenge_response = NTLMAuthChallengeResponse()
    negotiate['domain_name'] = domain.encode('utf-16le')
    negotiate['user_name'] = username.encode('utf-16le')
    challenge_response['server_challenge'] = challenge
    challenge_response['ntlmv2_client_challenge'] = b'\x00' * 8
    challenge_response['flags'] = 0x8201
    challenge_response['ntlmv2_response'] = ntlmv2_response

    # Build the NTLMv2 authentication request
    negotiate_data = negotiate.getData()
    challenge_response_data = challenge_response.getData()
    auth_data = negotiate_data + challenge_response_data

    # Crack the NTLMv2 hash using the authentication request and the LM hash
    from impacket.ntlm import getNTLMv2Response
    response, _ = getNTLMv2Response(auth_data, lm_hash, '', '', '', '', '', '', '', '', '', '')
    if response == ntlmv2_hash:
        return lm_hash.decode('utf-16le')

    return None

# Example usage
ntlmv2_hash = '4a4c4e4f4d4b4d4c4d4e4f4d4b4d4c4'
challenge = bytes.fromhex('010100000000000000000000000000000000000000000000')
username = 'username'
domain = 'domain'
lmhash = 'aad3b435b51404eeaad3b435b51404ee'

password = crack_ntlmv2_hash(ntlmv2_hash, challenge, username, domain, lmhash)
print('Password:', password)
