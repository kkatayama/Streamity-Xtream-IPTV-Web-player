<?php
$db_url = "localhost";
$db_name = "starr2"; //database name
$db_username = "mangoboat"; //database account username
$db_password = "smokekush2"; //database account password
$epg_url = "http://star.iptvpanel.xyz/epg.php?username=TWertZrCsR&password=HbfSEZCZyx"
// $epg_url = "http://line.lemotv.cc/epg.php?username=3S6ySq44tg&password=6345364334434"; //epg xml url (http://domain.com:80/xmltv.php?username=pippo&password=test)
$epg_valid_hours = "+12 hours"; //if database has epg available for less than 12 hours it will be updated. Alternative values: "+1 day", "+2 days", "+1 week" etc etc

//To avoid wasting server resources, epg update will be triggered when an user login and database has less than 12 hours of programmes.

?>
