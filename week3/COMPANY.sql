/* =========================================================
   HeartiHealth Database Queries
   Based strictly on inserted data & given schema
   ========================================================= */


/* 1. Get all the predictions */
SELECT * FROM cardiodiagnosis;


/* 2. Get all the predictions for the day */
SELECT *
FROM cardiodiagnosis
WHERE DATE(date) = CURRENT_DATE;


/* 3. Get predictions for the day sorted by detection */
SELECT *
FROM cardiodiagnosis
WHERE DATE(date) = CURRENT_DATE
ORDER BY cardioarrestdetected DESC;


/* 4. Get all unique cities */
SELECT DISTINCT city
FROM addressinfo;


/* 5. Members from city 'Burgos' */
SELECT *
FROM memberinfo m
JOIN addressinfo a
ON m.member_id = a.memberinfo_member_id
WHERE a.city = 'Burgos';


/* 6. Members from city 'Flora' */
SELECT *
FROM memberinfo m
JOIN addressinfo a
ON m.member_id = a.memberinfo_member_id
WHERE a.city = 'Flora';


/* 7. Total blood tests done for Aisha */
SELECT COUNT(*) AS total_tests
FROM bloodtest b
JOIN cardiodiagnosis c ON b.cardiodiagnosis_cardio_id = c.cardio_id
JOIN memberinfo m ON c.memberinfo_member_id = m.member_id
WHERE m.firstname = 'aisha';


/* 8. X-ray details of Ajay whose cardio test was done on 26-Jan-2019 */
SELECT x.*
FROM xray x
JOIN cardiodiagnosis c ON x.cardiodiagnosis_cardio_id = c.cardio_id
JOIN memberinfo m ON c.memberinfo_member_id = m.member_id
WHERE m.firstname = 'ajay'
AND DATE(c.date) = '2019-01-26';


/* 9. Members from cities 'Burgos' and 'Flora' */
SELECT DISTINCT m.*
FROM memberinfo m
JOIN addressinfo a
ON m.member_id = a.memberinfo_member_id
WHERE a.city IN ('Burgos','Flora');


/* 10. Total blood tests done for Aberson */
SELECT COUNT(*) AS total_tests
FROM bloodtest b
JOIN cardiodiagnosis c ON b.cardiodiagnosis_cardio_id = c.cardio_id
JOIN memberinfo m ON c.memberinfo_member_id = m.member_id
WHERE m.lastname = 'aberson';


/* 11. Address details for member ID M303 */
SELECT *
FROM addressinfo
WHERE memberinfo_member_id = 'M303';


/* 12. X-ray details for cardio ID CID122 */
SELECT *
FROM xray
WHERE cardiodiagnosis_cardio_id = 'cid122';


/* 13. Symptom details for cardio ID CID250 and CID300 */
SELECT *
FROM symptom
WHERE cardiodiagnosis_cardio_id IN ('cid250','cid300');


/* 14. Symptom details for July 2019 */
SELECT *
FROM symptom
WHERE date >= '2019-07-01'
AND date < '2019-08-01';



/* 15. X-ray details for member with last name 'dailley' */
SELECT x.*
FROM xray x
JOIN cardiodiagnosis c ON x.cardiodiagnosis_cardio_id = c.cardio_id
JOIN memberinfo m ON c.memberinfo_member_id = m.member_id
WHERE m.lastname = 'dailley';


/* 16. Wearable device data for cardio IDs between CID100 and CID200 */
SELECT *
FROM wearabledevicedata
WHERE cardiodiagnosis_cardio_id BETWEEN 'CID100' AND 'CID200';


/* 17. Cardio diagnosis where first name starts with 'a' */
SELECT c.*
FROM cardiodiagnosis c
JOIN memberinfo m ON c.memberinfo_member_id = m.member_id
WHERE m.firstname LIKE 'a%';


/*/ 18. Cardio diagnosis where first name starts with 'a' and ends with 'a' */
SELECT c.*
FROM cardiodiagnosis c
JOIN memberinfo m ON c.memberinfo_member_id = m.member_id
WHERE m.firstname LIKE 'a%a';


/* 19. Get all members */
SELECT * FROM memberinfo;


/* 20. Get all addresses */
SELECT * FROM addressinfo;


/* 21. Get wearable device information */
SELECT * FROM wearabledevicedata;


/* 22. Get all blood tests */
SELECT * FROM bloodtest;


/* 23. Members aged above 50 */
SELECT *
FROM memberinfo
WHERE age > 50;


/* 24. Addresses for city 'Flora' */
SELECT *
FROM addressinfo
WHERE city = 'Flora';


/* 25. Unique states */
SELECT DISTINCT state
FROM addressinfo;


/* 26. Total number of members */
SELECT COUNT(*) AS total_members
FROM memberinfo;


/* 27. Total number of blood tests */
SELECT COUNT(*) AS total_bloodtests
FROM bloodtest;


/* 28. Average cholesterol level */
SELECT AVG(serumcholesterol) AS avg_cholesterol
FROM bloodtest;


/* 29. Maximum oldpeak value */
SELECT MAX(oldpeak) AS max_oldpeak
FROM symptom;


/* 30. Tests done between Jan 1, 2015 and Jan 31, 2019 */
SELECT *
FROM cardiodiagnosis
WHERE date BETWEEN '2015-01-01' AND '2019-01-31';


/*/ 31. Male and female count aged 50–60 */
SELECT gender, COUNT(*) AS total
FROM memberinfo
WHERE age BETWEEN 50 AND 60
GROUP BY gender;


/* 32. Tests where blood pressure is between 100 and 200 */
SELECT *
FROM bloodtest
WHERE bloodpressure BETWEEN 100 AND 200;


/* 33. List of symptoms diagnosed */
SELECT * FROM symptom;


/* 34. Average age of patients */
SELECT AVG(age) AS avg_age
FROM memberinfo;


/* 35. Total cities for each state */
SELECT state, COUNT(DISTINCT city) AS total_cities
FROM addressinfo
GROUP BY state;


/* 36. Patient count by age groups */ READ ONCE
SELECT
CASE
 WHEN age BETWEEN 10 AND 20 THEN '10-20'
 WHEN age BETWEEN 20 AND 30 THEN '20-30'
 WHEN age BETWEEN 30 AND 40 THEN '30-40'
 WHEN age BETWEEN 40 AND 50 THEN '40-50'
 WHEN age BETWEEN 50 AND 60 THEN '50-60'
 WHEN age BETWEEN 60 AND 70 THEN '60-70'
END AS age_group,
COUNT(*) AS total
FROM memberinfo
GROUP BY age_group;


/* 37. Members and their addresses */
SELECT m.*, a.*
FROM memberinfo m
JOIN addressinfo a
ON m.member_id = a.memberinfo_member_id;


/* 38. Members and their cardio history */
SELECT m.*, c.*
FROM memberinfo m
JOIN cardiodiagnosis c
ON m.member_id = c.memberinfo_member_id;


/* 39. Members and their diseases */
SELECT m.*, d.*
FROM memberinfo m
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
JOIN diseasedetail d ON c.cardio_id = d.cardiodiagnosis_cardio_id;


/* 40. Females diagnosed with heart attack */
SELECT DISTINCT m.*
FROM memberinfo m
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
WHERE m.gender = '0'
AND c.cardioarrestdetected = 1;


/* 41. Female members above 50 with cardio info */
SELECT m.*, c.*
FROM memberinfo m
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
WHERE m.gender = '0'
AND m.age > 50;


/* 42. Males with BP > 140 and no heart attack */
SELECT DISTINCT m.*
FROM memberinfo m
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
JOIN bloodtest b ON c.cardio_id = b.cardiodiagnosis_cardio_id
WHERE m.gender = '1'
AND b.bloodpressure > 140
AND c.cardioarrestdetected = 0;


/* 43. Members with heart attack from Mountain Province */
SELECT DISTINCT m.*
FROM memberinfo m
JOIN addressinfo a ON m.member_id = a.memberinfo_member_id
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
WHERE a.state = 'Mountain Province'
AND c.cardioarrestdetected = 1;


/* 44. Male members (<40) with diseases and symptoms */
SELECT DISTINCT m.*, d.*, s.*
FROM memberinfo m
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
JOIN diseasedetail d ON c.cardio_id = d.cardiodiagnosis_cardio_id
JOIN symptom s ON c.cardio_id = s.cardiodiagnosis_cardio_id
WHERE m.gender = '1'
AND m.age < 40;


/* 45. Count from Mountain Province aged 50–60 */
SELECT COUNT(*) AS total
FROM memberinfo m
JOIN addressinfo a ON m.member_id = a.memberinfo_member_id
WHERE a.state = 'Mountain Province'
AND m.age BETWEEN 50 AND 60;


/* 46. Male and female count with BP > 140 and heart attack */
SELECT m.gender, COUNT(*) AS total
FROM memberinfo m
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
JOIN bloodtest b ON c.cardio_id = b.cardiodiagnosis_cardio_id
WHERE b.bloodpressure > 140
AND c.cardioarrestdetected = 1
GROUP BY m.gender;


/* 47. Average BP for age group 40–60 */
SELECT AVG(b.bloodpressure) AS avg_bp
FROM bloodtest b
JOIN cardiodiagnosis c ON b.cardiodiagnosis_cardio_id = c.cardio_id
JOIN memberinfo m ON c.memberinfo_member_id = m.member_id
WHERE m.age BETWEEN 40 AND 60;


/* 48. Diseases for BP 120–180 sorted by gender */
SELECT m.gender, d.*
FROM memberinfo m
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
JOIN bloodtest b ON c.cardio_id = b.cardiodiagnosis_cardio_id
JOIN diseasedetail d ON c.cardio_id = d.cardiodiagnosis_cardio_id
WHERE b.bloodpressure BETWEEN 120 AND 180
ORDER BY m.gender;


/* 49. X-ray count per month from Special Provinces */ RECHECK 
SELECT MONTH(x.date) AS month, COUNT(*) AS total_xrays
FROM xray x
JOIN cardiodiagnosis c ON x.cardiodiagnosis_cardio_id = c.cardio_id
JOIN memberinfo m ON c.memberinfo_member_id = m.member_id
JOIN addressinfo a ON m.member_id = a.memberinfo_member_id
WHERE a.state = 'Special Provinces'
GROUP BY MONTH(x.date);


/* 50. Average age of heart-attack patients per state and gender */
SELECT a.state, m.gender, AVG(m.age) AS avg_age
FROM memberinfo m
JOIN addressinfo a ON m.member_id = a.memberinfo_member_id
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
WHERE c.cardioarrestdetected = 1
GROUP BY a.state, m.gender;


/* 51. Count per state with heart attack, slope=2, X-ray & symptom */
SELECT a.state, COUNT(DISTINCT m.member_id) AS total_people
FROM memberinfo m
JOIN addressinfo a ON m.member_id = a.memberinfo_member_id
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
JOIN wearabledevicedata w ON c.cardio_id = w.cardiodiagnosis_cardio_id
JOIN xray x ON c.cardio_id = x.cardiodiagnosis_cardio_id
JOIN symptom s ON c.cardio_id = s.cardiodiagnosis_cardio_id
WHERE c.cardioarrestdetected = 1
AND w.slope = 2
GROUP BY a.state;
