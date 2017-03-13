SELECT
   TIMESTAMPDIFF(
      SECOND,
      from_unixtime(`triggers`.lastchange),
      CURRENT_TIMESTAMP ()
   ) AS second_diff,
   `triggers`.triggerid AS tid,
   `triggers`.description,
   `triggers`.`status`,
   `triggers`.priority,
   `triggers`.lastchange,
   from_unixtime(`triggers`.lastchange) AS lasttime,
   from_unixtime(`items`.lastclock) AS changetime,
   `items`.units,
   `items`.hostid,
   `hosts`.`host`,
--    `hosts`.n_location,
   `hosts`.host,
--    `hosts`.n_url,
   `triggers`.expression,
   items.lastvalue,
   FROM_UNIXTIME(`events`.clock) AS clock,
   `events`.objectid,
   `events`.eventid,
   MAX(`events`.eventid) AS eid,
   `events`.acknowledged,

IF (
   (
      SELECT
         acknowledged
      FROM
         `events`
      WHERE
         objectid = tid
      ORDER BY
         eventid DESC
      LIMIT 1
   ) = 0,
   'N',
   'Y'
) AS n_acknowledged
FROM
   `triggers`
INNER JOIN functions ON `triggers`.triggerid = functions.triggerid
INNER JOIN items ON functions.itemid = items.itemid
INNER JOIN `hosts` ON items.hostid = `hosts`.hostid
LEFT JOIN `events` ON `events`.objectid = `triggers`.triggerid
WHERE
   `triggers`.`value` = 1
AND `triggers`.priority != 1
AND `hosts`. STATUS = 0
AND `events`.`object` = 0
AND `events`.`value` = 1
GROUP BY
   functions.triggerid
ORDER BY
   lasttime,
   clock DESC
