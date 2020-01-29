mkdir coco
cd coco
mkdir images
cd images

wget http://images.cocodataset.org/zips/train2014.zip
unzip train2014.zip
rm train2014.zip

wget http://images.cocodataset.org/zips/val2017.zip
unzip val2017.zip
rm val2017.zip

# wget http://images.cocodataset.org/zips/test2017.zip
# unzip test2017.zip
# rm test2017.zip

# cd ../
# wget http://images.cocodataset.org/annotations/annotations_trainval2017.zip
# wget http://images.cocodataset.org/annotations/stuff_annotations_trainval2017.zip
# wget http://images.cocodataset.org/annotations/image_info_test2017.zip

# unzip annotations_trainval2017.zip
# unzip stuff_annotations_trainval2017.zip
# unzip image_info_test2017.zip

# rm annotations_trainval2017.zip
# rm stuff_annotations_trainval2017.zip
# rm image_info_test2017.zip


# cd train2014
# mkdir labellabel

# cd ../val2017
# mkdir labellabel
cd /home/ec2-user
mkdir weights

git clone https://github.com/azadyasar/COCO---YOLO.git
cd COCO---YOLO/drive-download-20200127T073021Z-001/
mv coco.data yolo.cfg /home/ec2-user/

cd ..
mv labellabel-20200128T052301Z-001.zip /home/ec2-user/dataset/coco/images/train2014/
cd /home/ec2-user/dataset/coco/images/train2014/
unzip labellabel-20200128T052301Z-001.zip
rm labellabel-20200128T052301Z-001.zip
cd -

mv labellabel-20200128T074745Z-001val.zip /home/ec2-user/dataset/coco/images/val2017/
cd /home/ec2-user/dataset/coco/images/val2017/
unzip labellabel-20200128T074745Z-001val.zip
rm labellabel-20200128T074745Z-001val.zip
cd -

python /home/ec2-user/COCO---YOLO/Scripts/names.py
python /home/ec2-user/COCO---YOLO/Scripts/filepaths.py