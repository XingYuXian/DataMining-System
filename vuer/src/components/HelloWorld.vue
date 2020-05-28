<template>
  <el-container>
    <el-header>
      <el-col class="hh">
        ☁ DataMining
      </el-col>


      </el-header>
    <el-container>
      <el-aside width="200px">
        <el-row class="tac">
          <el-col width = "200px">
            <el-menu
              default-active="2"
              class="el-menu-vertical-demo">
                <el-menu-item-group>
                  <el-menu-item index="1-1">上传数据</el-menu-item>
                  <el-menu-item index="1-2">个体画像</el-menu-item>
                  <el-menu-item index="1-3">群体画像</el-menu-item>
                </el-menu-item-group>
                </el-submenu>
            </el-menu>
          </el-col>
          </el-row>
        </el-aside>
      <el-main>
        Main
        </el-main>
    </el-container>
  </el-container>
  </template>



<script>
  export default {
    data(){
      return{
        
      };
    },
    methods: {
    }
  }
</script>


<style>
  html,body,#app,.el-container{
          padding: 0px;
          margin: 0px;
          height: 100%;
      }
  .el-header {
      background-color: #2b5d86;
      color: #ffffff;
      text-align: left;
      font-size: 20px;
      line-height: 60px;
      font-family:"fantasy";
    }

    .el-aside {
      background-color: #ffffff;
      color: #333;
      text-align: center;
      line-height: 200px;
      font-size: 0px;
    }

    .el-main {
      background-color: #E9EEF3;
      color: #333;
      text-align: center;
      line-height: 160px;
    }
    .tac{}
    .hh{
      margin-left: 25px;
    }
  </style>
