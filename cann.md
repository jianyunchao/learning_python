# CANN刷包安装

###	一、获取机器系统信息

####	内核架构信息
x86_64

aarch64

查看内核版本

```
cat /proc/version
uanme -a
uanme -r
```



####	linux机器版本信息

查看linux版本

```
lsb_release -a
cat /etc/issue
cat /etc/redhat-release
```



####	昇腾芯片信息

|      | 芯片类型                      | 用途     |
| ---- | ----------------------------- | -------- |
| 1    | ascend310                     | 训练资源 |
| 2    | ascend710（等同于ascend310P） | 推理资源 |
| 3    | ascend910                     | 推理资源 |



###	二、对应安装包获取



| 软件类型 | 软件介绍                                                     |
| -------- | ------------------------------------------------------------ |
| 固件     | 固件包含昇腾AI处理器自带的OS 、电源器件和功耗管理器件控制软件，分别用于后续加载到AI处理器的模型计算、芯片启动控制和功耗控制。 |
| 驱动     | 部署在昇腾服务器，功能类似英伟达驱动，管理查询昇腾AI处理器，同时为上层CANN软件提供芯片控制、资源分配等接口。 |
| CANN     | 部署在昇腾服务器，功能类似英伟达CUDA，包含Runtime、算子库、图引擎、媒体数据处理等组件，通过AscendCL（Ascend Computing Language）对外提供Device管理、Context管理、Stream管理、内存管理、模型加载与执行、算子加载与执行、媒体数据处理等API，帮助开发者实现在昇腾CANN平台上进行深度学习推理计算、图像预处理、单算子加速计算。 |

####	整包安装



官网：https://www.mindspore.cn/install



版本构建仓安装简介：

wget --user mindspore --password mindspore@logs\!\#123 http://124.70.19.41/ascend/ascend910/20221214/CANN/x86_64/xxx.run



wget --user mindspore --password mindspore@repo!%23123



####	分包安装

对应关系：

|      | 驱动C版本 | 商用版本 | 固件（通用社区分支版本） | CANN包 | MindSpore版本 |
| ---- | --------- | -------- | ------------------------ | ------ | ------------- |
| 1    | C29       | 22.0.RC3 | CANN 6.0.1.RC1.alpha005  | 6.4    | 2.0.X         |
| 2    | C84       | 22.0.0   | CANN 6.0.1.alpha001      | 1.84   | 1.10.X        |
| 3    | C83       | 22.0.RC3 | CANN 5.1.RC2.alpha005    | 1.83   | 1.9.X         |
| 4    | C82       | 22.0.RC2 | CANN 5.1.RC2.alpha008    | 1.82   | 1.8.X         |



查看现有安装版本：

```
# ascend版本
cat /usr/local/Ascend/version.info
# version=22.0.3.b080


# 驱动版本
cat /usr/local/Ascend/driver
# Version=22.0.3.b080
# ascendhal_version=6.13.22
# aicpu_version=1.0
# tdt_version=1.0
# log_version=1.0
# prof_version=2.0
# dvppkernels_version=1.1
# tsfw_version=1.0
# Innerversion=V100R001C83SPC001B228  # C83对应mindspore1.9.x，C版本可以对应驱动与mindspore，向下兼容
# package_version=6.0.rc1


# 固件版本
cat /usr/local/Ascend/firmware
# Version=1.83.9.1.228
# firmware_version=1.0
# package_version=6.0.rc1

# CANN版本
cat /usr/local/Ascend/CANN-*
```





升级：

firmware->deriver->runtime->compiler->opp->opp_kernel->others(toolkit,aicpu)



### 三、run包安装命令

####	整包安装（driver+firmware+toolkit)

安装包来源：官网申请

```
bash xxx.run --full

```





####	分包安装（driver+firmware+各分包）

安装包来源：社区下载

| 分包名         | 内容                                    | MindSpore需要 |
| -------------- | --------------------------------------- | ------------- |
| firmware       | Ascend硬件固件                          | 需要          |
| driver         | Ascend硬件驱动                          | 需要          |
| CANN-runtime   | Runtime库，曾经的aclib库部分fwkplugin库 | 需要          |
| CANN-compiler  | Complier库，曾经的fwkacllib库，构建需要 | 需要          |
| CANN-fwkplugin | Ascend适配TF插件                        | 不需要        |
| CANN-toolkit   | 调测工具                                | 调测时需要    |
| CANN-aoe       | 调测工具                                | 调测时需要    |
| CANN-opp       | TBE算子                                 | 需要          |
| opp_kernel     | 预编译算子包                            | 需要          |
| aicpu          | Aicpu算子                               | 需要          |





升级固件查看命令	

```
# 系统版本
/usr/local/Ascend/driver/tools/upgrade-tool --device_index -1 --system_version
控制台打印：
{
Get system version(22.0.3) succeed, deviceId(0)
        {"device_id":0, "version":22.0.3}
Get system version(22.0.3) succeed, deviceId(1)
        {"device_id":1, "version":22.0.3}
Get system version(22.0.3) succeed, deviceId(2)
        {"device_id":2, "version":22.0.3}
Get system version(22.0.3) succeed, deviceId(3)
        {"device_id":3, "version":22.0.3}
}

# 组件版本
/usr/local/Ascend/driver/tools/upgrade-tool --device_index -1 --component -1 --version
控制台打印：
{
Get component version(1.83.10.1.248) succeed for deviceId(0), componentType(0).
        {"device_id":0, "component":nve, "version":1.83.10.1.248}
Get component version(1.83.10.1.248) succeed for deviceId(0), componentType(1).
        {"device_id":0, "component":xloader, "version":1.83.10.1.248}
Get component version(1.77.20.0.B200) succeed for deviceId(0), componentType(2).
        {"device_id":0, "component":m3fw, "version":1.77.20.0.B200}
Get component version(1.83.10.1.248) succeed for deviceId(0), componentType(3).
        {"device_id":0, "component":uefi, "version":1.83.10.1.248}
Get component version(1.77.20.0.B200) succeed for deviceId(0), componentType(4).
        {"device_id":0, "component":tee, "version":1.77.20.0.B200}
Get component version(1.83.10.1.248) succeed for deviceId(1), componentType(0).
        {"device_id":1, "component":nve, "version":1.83.10.1.248}
Get component version(1.83.10.1.248) succeed for deviceId(1), componentType(1).
        {"device_id":1, "component":xloader, "version":1.83.10.1.248}
Get component version(1.77.20.0.B200) succeed for deviceId(1), componentType(2).
        {"device_id":1, "component":m3fw, "version":1.77.20.0.B200}
Get component version(1.83.10.1.248) succeed for deviceId(1), componentType(3).
        {"device_id":1, "component":uefi, "version":1.83.10.1.248}
Get component version(1.77.20.0.B200) succeed for deviceId(1), componentType(4).
        {"device_id":1, "component":tee, "version":1.77.20.0.B200}
Get component version(1.83.10.1.248) succeed for deviceId(2), componentType(0).
        {"device_id":2, "component":nve, "version":1.83.10.1.248}
Get component version(1.83.10.1.248) succeed for deviceId(2), componentType(1).
        {"device_id":2, "component":xloader, "version":1.83.10.1.248}
Get component version(1.77.20.0.B200) succeed for deviceId(2), componentType(2).
        {"device_id":2, "component":m3fw, "version":1.77.20.0.B200}
Get component version(1.83.10.1.248) succeed for deviceId(2), componentType(3).
        {"device_id":2, "component":uefi, "version":1.83.10.1.248}
Get component version(1.77.20.0.B200) succeed for deviceId(2), componentType(4).
        {"device_id":2, "component":tee, "version":1.77.20.0.B200}
Get component version(1.83.10.1.248) succeed for deviceId(3), componentType(0).
        {"device_id":3, "component":nve, "version":1.83.10.1.248}
Get component version(1.83.10.1.248) succeed for deviceId(3), componentType(1).
        {"device_id":3, "component":xloader, "version":1.83.10.1.248}
Get component version(1.77.20.0.B200) succeed for deviceId(3), componentType(2).
        {"device_id":3, "component":m3fw, "version":1.77.20.0.B200}
Get component version(1.83.10.1.248) succeed for deviceId(3), componentType(3).
        {"device_id":3, "component":uefi, "version":1.83.10.1.248}
Get component version(1.77.20.0.B200) succeed for deviceId(3), componentType(4).
        {"device_id":3, "component":tee, "version":1.77.20.0.B200}
}

# driver版本号查询
cat /usr/local/Ascend/driver/version.info
控制台展示：
Version=22.0.3
ascendhal_version=6.14.24
aicpu_version=1.0
tdt_version=1.0
log_version=1.0
prof_version=2.0
dvppkernels_version=1.1
tsfw_version=1.0
Innerversion=V100R001C83SPC001B249
package_version=6.0.rc1

```







验证

1. 验证lite
   source py37_env.sh
   cd lite_script
   sh dbnet_res18.sh

2. 验证mindocr
   mindocr --input_images_dir=/home/mindocr/datasets/small_samples/images --device=Ascend310 --device_id=1 --parallel_num=2 --det_model_path=/home/mindocr/lianghao/ckpt/om/v2/dbnet/dbnet_dynamic_dims_100.om --cls_model_path=/home/mindocr/lianghao/ckpt/om/v2/cls_310.om --rec_model_path=/home/mindocr/lianghao/ckpt/om/v2/crnn/ --rec_char_dict_path=/home/mindocr/lianghao/ckpt/om/ppocr_keys_v1.txt --res_save_dir=./result1  --vis_pipeline_save_dir=result3





/home/mindocr/Ascend/ascend-toolkit/latest/CANN-6.3







升级安装

固件

[INFO]Firmware package has been installed on the path /usr/local/Ascend, the version is 1.83.10.1.248, and the version of this package is 1.84.T10.0.B207,do you want to continue?  [y/n]

驱动

[INFO]Driver package has been installed on the path /usr/local/Ascend, the version is 22.0.3, and the version of this package is 22.0.4.b080,do you want to continue?  [y/n]







```
pip list | grep mindspore

CPU版本：mindspore
Ascend版本：mindspore-ascend
GPU版本：mindspore-gpu

```

