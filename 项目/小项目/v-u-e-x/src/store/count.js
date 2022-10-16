//求和组件
export default {
	namespaced: true,
	actions: {
		incrementOdd(context, value) {
			if (context.state.sum % 2) {
				context.commit('INCREMENT', value)
				// console.log(context)
			}
		},
		incrementWait(context, value) {
			setTimeout(() => {
				context.commit('INCREMENT', value)
			}, 1000)
		}
	},
	mutations: {
		INCREMENT(state, value) {
			state.sum += value
		},
		DECREMENT(state, value) {
			state.sum -= value
		},
		MULTIPLY(state, value) {
			state.sum *= value * 10
		}
	},
	state: {
		sum: 0,
		school: '蓝翔',
		subject: '挖掘机'
	},
	getters: {
		bigSum(state) {
			return state.sum * 10
		}
	}
}
