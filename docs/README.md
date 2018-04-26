
# Minecraft Server Advertiser

A Package to find and advertise Minecraft servers to the LAN like single player->open to lan works.

Minestat is forked from [ldilley](https://github.com/ldilley/minestat). See below for their PHP/Python readme extract

## minestat

A Minecraft server status checker

You can use these classes/modules in a monitoring script to poll multiple Minecraft servers or to let
visitors see the status of your server from their browser.

### PHP example
```php
<?php
require_once('minestat.php');

$ms = new MineStat("minecraft.dilley.me", 25565);
printf("Minecraft server status of %s on port %s:<br>", $ms->get_address(), $ms->get_port());
if($ms->is_online())
{
  printf("Server is online running version %s with %s out of %s players.<br>", $ms->get_version(), $ms->get_current_players(), $ms->get_max_players());
  printf("Message of the day: %s<br>", $ms->get_motd());
}
else
{
  printf("Server is offline!<br>");
}
?>
```

### Python example
```python
import minestat

ms = minestat.MineStat('minecraft.dilley.me', 25565)
print('Minecraft server status of %s on port %d:' % (ms.address, ms.port))
if ms.online:
  print('Server is online running version %s with %s out of %s players.' % (ms.version, ms.current_players, ms.max_players))
  print('Message of the day: %s' % ms.motd)
else:
  print('Server is offline!')
```

```
