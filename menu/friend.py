def acc_all_friend():
	confirm_execute()
	gas = Friend()
	gas.dump_sts("https://mbasic.facebook.com/friends/center/requests/", "Konfirmasi", "Lihat selengkapnya", 0, "com")
	print()
	echo("[+] Total: " + str(len(gas.id)))
	gas.hajar()
	print()
	echo("[+] Done!")
	enter()

def rej_all_friend():
	confirm_execute()
	gas = Friend()
	gas.dump_sts("https://mbasic.facebook.com/friends/center/requests/", "Hapus Permintaan", "Lihat selengkapnya", 0, "com")
	print()
	echo("[+] Total: " + str(len(gas.id)))
	gas.hajar()
	print()
	echo("[+] Done!")
	enter()
	
def unadd_all_friend():
	confirm_execute()
	gas = Friend()
	gas.dump_sts("https://mbasic.facebook.com/friends/center/requests/outgoing/", "Batalkan Permintaan", "Lihat selengkapnya", 0, "com")
	print("\n   [+] Total: " + str(len(gas.id)))
	gas.hajar()
	print()
	echo("[+] Done!")
	enter()

def delete_all_friend():
	confirm_execute()
	gas = Friend()
	gas.dump_sts_wclass("https://mbasic.facebook.com/me/friends", True, "Lihat Teman Lain", 0, "fr_tab", href_na=True, req=False)
	print()
	echo("[+] Total: " + str(len(gas.id)))
	gas.delete_all_friend()
	print()
	echo("[+] Done!")
	enter()