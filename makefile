
mod/zlibmodule.o: mod/zlibmodule.c
	gcc -pthread -fno-strict-aliasing -DNDEBUG -g -fwrapv -O2 -Wall -Wstrict-prototypes -fPIC -I/usr/include/python2.6 -c $< -o $@

mod/zlib.so: mod/zlibmodule.o
	gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions $^ -o $@
	
all: mod/zlib.so

clean:
	-rm mod/*.so
	-rm mod/*.o
