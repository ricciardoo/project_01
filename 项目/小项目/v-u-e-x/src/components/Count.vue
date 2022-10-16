<template>
	<div>
		<h1>当前求和为：{{ sum }}</h1>
		<h2>放大10倍后的值是：{{ bigSum }}</h2>
		<h2>我在{{ school }}学习{{ subject }}</h2>
		<h2>下方组件总人数是：{{ personList.length }}</h2>
		<select v-model.number="n">
			<option value="1">1</option>
			<option value="2">2</option>
			<option value="3">3</option>
		</select>
		<button @click="increment(n)">点我加</button>
		<button @click="decrement(n)">点我减</button>
		<button @click="incrementOdd(n)">当前求和为奇数再加</button>
		<button @click="incrementWait(n)">等一秒再加</button>
	</div>
</template>

<script>
import { mapState, mapGetters, mapMutations, mapActions } from 'vuex'
export default {
	name: 'Count',
	data() {
		return {
			n: 1 //用户选择的数字
		}
	},
	computed: {
		//array form
		...mapState('countAbout', ['sum', 'subject', 'school']),
		...mapState('personAbout', ['personList']),
		...mapGetters('countAbout', ['bigSum'])
		//object form
		// ...mapState({ sum: 'sum', subject: 'subject', school: 'school' }),
		// ...mapGetters({ bigSum: 'bigSum' })

		// sum() {
		// 	return this.$store.state.sum
		// },
		// school() {
		// 	return this.$store.state.school
		// },
		// subject() {
		// 	return this.$store.state.subject
		// },
		// bigSum() {
		// 	return this.$store.getters.bigSum
		// }
	},
	methods: {
		...mapMutations('countAbout', { increment: 'INCREMENT', decrement: 'DECREMENT' }),
		...mapActions('countAbout', { incrementOdd: 'incrementOdd', incrementWait: 'incrementWait' })

		// increment() {
		// 	this.$store.commit('INCREMENT', this.n)
		// },
		// decrement() {
		// 	this.$store.commit('DECREMENT', this.n)
		// },

		// incrementOdd() {
		// 	this.$store.dispatch('incrementOdd', this.n)
		// },
		// incrementWait() {
		// 	this.$store.dispatch('incrementWait', this.n)
		// },
	},
	mounted() {}
}
</script>

<style lang="css" scoped>
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

div {
	padding: 10px 30px 30px 30px;
	width: 660px;
	height: 300px;
	background-color: antiquewhite;
}

select {
	width: 60px;
	height: 40px;
	border-radius: 5px;
	font-weight: 700;
	text-align: center;
}
</style>
