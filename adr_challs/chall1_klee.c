#include <klee/klee.h>
#include <assert.h>

char privKey[4];
const int privKeyLen = 4;

char publKey[] = {
	0x04, 0x02, 0x01, 0x01, 0x07, 0x01, 0x01, 0x01, 0x05, 0x02, 0x01, 0x01, 0x05, 0x01, 0x01, 0x00, 0x04, 0x02, 0x01, 0x01, 0x04, 0x02, 0x01, 0x01
};
char secret[] = {
	0x10, 0x00, 0x1c, 0x04, 0x04, 0x1f, 0x1f, 0x01, 0x0a, 0x15, 0x1c, 0x11, 0x0a, 0x1f, 0x2c, 0x43, 0x04, 0x05, 0x1b, 0x01, 0x0f, 0x01, 0x0c, 0x39
};
char known[] = "TDOH{";
char flag[sizeof publKey]; /* flag type: TDOH{...XXXXXXXXXXXXXXXX...} */

int main(void) {
	klee_make_symbolic(flag, sizeof flag, "flag");
	klee_make_symbolic(privKey, 4, "privKey");

	for(int i = 0; i < 5; i++) {
		klee_assume(flag[i] == known[i]);
	}

	for(int i = 0; i < sizeof(publKey); i++) {
		klee_assume(publKey[i] == flag[i] / privKey[i % privKeyLen]);
		klee_assume(secret[i] == flag[i] - (publKey[i] * privKey[i % privKeyLen]));
	}

	klee_assert(0);
}

/*
 * === LazyKLEE ===
 * [+] Creating container...
 * 72f646f96555e71b3ef5bd0591bb73393b886c6b0c40fb019a95853aa1558302
 *
 * [+] Compiling llvm bitcode...
 *
 *
 * [+] Running KLEE...
 * [+] ASSERTION triggered!
 * ktest file : './klee-last/test000002.ktest'
 * args       : ['./out.bc']
 * num objects: 2
 * object    0: name: b'flag'
 * object    0: size: 24
 * object    0: data: b'TDOH{ARE_YOU_A_CHINESE?}'
 * object    1: name: b'privKey'
 * object    1: size: 4
 * object    1: data: b'\x11"3D'
 *
 * [+] Removing container...
 */
