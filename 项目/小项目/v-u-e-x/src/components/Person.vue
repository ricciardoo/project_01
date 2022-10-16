<template>
	<div>
		<h2>人员列表</h2>
		<input type="text" placeholder="请输入姓名" v-model="name" />
		<button @click="add">提交</button>
		<button @click="addWang">添加一个姓王的人</button>
		<button @click="randomSentence">随机句子</button>
		<h2>上方组件的求和为：{{ sum }}</h2>
		<h2>第一个人的名字是：{{ firstPersonName }}</h2>

		<ol>
			<li v-for="p in personList" :key="p.id">{{ p.name }}</li>
		</ol>
	</div>
</template>

<script>
import { nanoid } from 'nanoid'
import { mapState } from 'vuex'
export default {
	name: 'Person',

	data() {
		return {
			name: ''
		}
	},

	computed: {
		personList() {
			return this.$store.state.personAbout.personList
		},
		// sum() {
		// 	return this.$store.state.countAbout.sum
		// }
		...mapState('countAbout', ['sum']),
		firstPersonName() {
			return this.$store.getters['personAbout/firstPersonName']
		}
	},

	methods: {
		add() {
			const personObj = { id: nanoid(), name: this.name }
			this.$store.commit('personAbout/ADD_PERSON', personObj)
			this.name = ''
		},
		addWang() {
			const personObj = { id: nanoid(), name: this.name }
			this.$store.dispatch('personAbout/addPersonWang', personObj)
			this.name = ''
		},
		randomSentence() {
			this.$store.dispatch('personAbout/addPersonServer')
		}
	}
}
</script>

<style lang="css" scoped>
div {
	padding: 30px;
	width: 660px;
	height: 300px;
	background-color: cadetblue;
}

button {
	margin-left: 10px;
	box-shadow: 3px 4px 0px 0px #1564ad;
	background: linear-gradient(to bottom, #79bbff 5%, #378de5 100%);
	background-color: #79bbff;
	border-radius: 5px;
	border: 1px solid #337bc4;
	display: inline-block;
	cursor: pointer;
	color: #ffffff;
	font-family: Arial;
	font-size: 14px;
	font-weight: bold;
	padding: 7px 27px;
	text-decoration: none;
	text-shadow: 0px 1px 0px #528ecc;
}

Button:hover {
	background: linear-gradient(to bottom, #378de5 5%, #79bbff 100%);
	background-color: #378de5;
}

Button:active {
	position: relative;
	top: 1px;
}

input {
	width: 200px;
	height: 30px;
	border-radius: 5px;
	padding-left: 10px;
}
</style>
