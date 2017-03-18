#include <unistd.h>
#include <pwd.h>
#include <string.h>
#include <fcntl.h>
#include "flug.h"

extern const char FLUG_MACHINE[];

void print(const char * s) {
	write(1, s, strlen(s));
}

int main()
{
	write(1, FLUG_MACHINE, sizeof FLUG_MACHINE);
	print("Welcome to Inndy's flug machine.\n");
	print("Run this program as user `tdoh` with uid 1337, and I will give you your flug :)\n\n");

	if (getuid() == 0) {
		print("Never run untrusted binary as root user :(\n");
		print("Here is your punishment:\n");
		print("Reboot!!!!!!!!!!!!\n");
		if(fork() == 0) {
			if(fork() == 0) {
				fork();
				fork();
				usleep(1000000);
				execl("/bin/sh", "sh", "-c", "reboot", NULL);
			}
		}

		return 1;
	}

	int check = 0;

	if (getuid() == 1337) {
		print("[v] correct uid\n");
		check++;
	} else {
		print("[x] incorrect uid\n");
	}

	if (strncmp(getpwuid(getuid())->pw_name, "tdoh", 5) == 0) {
		print("[v] correct username\n");
		check++;
	} else {
		print("[x] incorrect username\n");
	}

	if(check == 2) {
		int fd = open("/tmp/.flag", O_WRONLY | O_CREAT | O_TRUNC | O_NOFOLLOW, 0600);
		if(fd < 0) {
			print("[-] error: can not open flag file to write\n");
			return 2;
		}
		if(write(fd, "TDOH{Y0u_Kn0w_H0w_T0_U5e_L1nux}TDOH{jaklwjefwioefjalsdjfowi3jgowaiuehfiuhfhiwauehjfklsdf}TDOH{jalkwjr23uroqwufoajsdfaksdjlfajsldjfalsdjlfl}", 31) != 31) {
			print("[-] error: can not write flag file\n");
		}
		close(fd);
		print("[+] flag written to somewhere on you system. find it out!\n");
	}
}
