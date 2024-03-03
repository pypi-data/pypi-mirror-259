ritual main() {
        a = alloc 8
        [a] = 0x4141
        b = write(1, a, 2)

        end b
}

