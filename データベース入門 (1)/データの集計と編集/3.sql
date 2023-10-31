-- データの更新
update prefectures set name = '茨城県' WHERE name = '茨木県';
update prefectures set name = '鳥取県' WHERE name = '取鳥県';
-- テーブルの情報を表示
select * from prefectures;
