#ifndef SCRYPT_H
#define SCRYPT_H

#ifdef __cplusplus
extern "C" {
#endif

void scrypt_1024_1_1_256(const char* input, char* output);
void scrypt_1024_1_1_256_sp(const char* input, char* output, char* scratchpad);

#ifdef __cplusplus
}
#endif

#endif
