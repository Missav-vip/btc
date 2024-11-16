// Konfigurasi VPN untuk masing-masing profil
const vpnConfig = {
    profile1: 'vpn-profile-1',
    profile2: 'vpn-profile-2',
    // Lanjutkan untuk 10 profil
};

function activateVPN(profileId) {
    const vpnProfile = vpnConfig['profile' + profileId];
    console.log('Mengaktifkan VPN untuk ' + vpnProfile);

    // Misalkan menggunakan ekstensi VPN
    // Ini hanya contoh, Anda harus menyesuaikan dengan ekstensi atau API VPN yang digunakan
    // browser.extension.sendMessage({ action: 'activate', profile: vpnProfile });
}
