# 4. Introduce a Pi-Hole for Local DNS

Date: 2020-06-20

## Status

Accepted

## Context

- I don't want to make the CoreDNS container in my cluster the local DNS source of truth, because my view of it is entirely for cluster DNS
- I don't want to expose my services to the internet _yet_ (but expect to later)
- I have a dedicated domain for my services
- I can set up TLS for "internal" domains via Let's Encrypt + CloudFlare DNS
- I need something to route internal requests to my cluster without querying external DNS resolvers, which won't know about my internal cluster
- I can probably do this on my UniFi setup, but it'd likely require some configuration outside of the controller software
- Pi-Hole introduces some other neat features
- I have multiple spare Raspberry Pis

## Decision

- Flash Raspberry Pi OS (minimal install) on a microSD card
- Use that card to boot a Raspberry Pi 3B+ (`Raspberry Pi 3 Model B Rev 1.2`)
- Configure for SSH, use wired LAN
  - Consider adding WLAN later, but Pi-Hole will expect a single static IP?
- Install and configure unattended upgrades
- Install Pi-Hole

## Consequences

- I'm not sure if I can have the Pi-Hole configured to work with MetalLB nicely
  - I don't need to know right away, I'll be starting with a simpler ingress setup

## Future Work

- Ensure unattended upgrades are working
- Forward update emails off the machine
- Auto update `cloudflared`

## Appendix

### Command History

```shell
### prerequisites etc.
sudo apt-get update -y && sudo apt-get dist-upgrade -y && sudo apt-get autoremove -y
sudo apt-get install -y unattended-upgrades apt-listchanges bsd-mailx \
  ufw \
  vim ssh-import-id \
  git
ssh-import-id-gh liamdawson
vim /etc/apt/apt.conf.d/50unattended-upgrades # see below for contents

### install pi-hole
curl -sSL https://install.pi-hole.net > install.sh
less install.sh
bash install.sh
sudo pihole -a -p # set a new password
echo 'BLOCKINGMODE=NXDOMAIN' | sudo tee -a /etc/pihole/pihole-FTL.conf >/dev/null
sudo systemctl restart pihole-FTL.service

### configure firewall
# ssh!
sudo ufw allow 22/tcp

# from pi-hole docs
(
sudo ufw allow 80/tcp
sudo ufw allow 53/tcp
sudo ufw allow 53/udp
sudo ufw allow 67/tcp
sudo ufw allow 67/udp
)

sudo ufw reject 443/tcp
sudo ufw enable

### setup DNS over HTTPS
curl -fSLO https://bin.equinox.io/c/VdrWdbjqyF/cloudflared-stable-linux-arm.tgz
tar -xvzf cloudflared-stable-linux-arm.tgz
sudo cp ./cloudflared /usr/local/bin
sudo chmod +x /usr/local/bin/cloudflared
rm cloudflare*
sudo mkdir /etc/cloudflared/
cat <<EOF | sudo tee /etc/cloudflared/config.yml >/dev/null
proxy-dns: true
proxy-dns-port: 5053
proxy-dns-upstream:
  - https://1.1.1.1/dns-query
  - https://1.0.0.1/dns-query
EOF
sudo cloudflared service install
sudo systemctl enable --now cloudflared
# test with: dig @127.0.0.1 -p 5053 google.com

# - set custom DNS ipv4 in the pi-hole to 127.0.0.1#5053
# - remove all other DNS servers
# - set conditional forwarding for local domain
```

### Unattended Upgrade Configuration

```conf
Unattended-Upgrade::Origins-Pattern {
        "origin=Debian,codename=${distro_codename},label=Debian";
        "origin=Debian,codename=${distro_codename},label=Debian-Security";
};

Unattended-Upgrade::Package-Blacklist {
};

Unattended-Upgrade::AutoFixInterruptedDpkg "true";
Unattended-Upgrade::MinimalSteps "true";
Unattended-Upgrade::InstallOnShutdown "false";
Unattended-Upgrade::Mail "root";
Unattended-Upgrade::Remove-New-Unused-Dependencies "true";
Unattended-Upgrade::Remove-Unused-Dependencies "true";
Unattended-Upgrade::Automatic-Reboot "true";
Unattended-Upgrade::Automatic-Reboot-WithUsers "true";
Unattended-Upgrade::Automatic-Reboot-Time "04:51";

// Set this value to "true" to get emails only on errors. Default
// is to always send a mail if Unattended-Upgrade::Mail is set
//Unattended-Upgrade::MailOnlyOnError "false";
```
