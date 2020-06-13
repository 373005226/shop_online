<template>
	<div v-if="showPopup" class="popup"  @touchmove.stop.prevent>
		<div :class="[ani, animation ? 'ani' : '', !custom ? 'custom' : '']" class="popup__mask" @click="close(true)" />
		<div :class="[ ani,'popup__wrapper',type, animation ? 'ani' : '', !custom ? 'custom' : '']" @click="close(true)">
			<div class="popup__wrapper-box" @click.stop="clear">
				<slot />
			</div>
		</div>
	</div>
</template>

<script>
	export default {
		name: 'Popup',
		props: {
			// 开启动画
			animation: {
				type: Boolean,
				default: true
			},
			// 弹出层类型，可选值，top: 顶部弹出层；bottom：底部弹出层；center：全屏弹出层
			type: {
				type: String,
				default: 'center'
			},
			// 是否开启自定义
			custom: {
				type: Boolean,
				default: true
			},
			// maskClick
			maskClick: {
				type: Boolean,
				default: true
			},
			show: {
				type: Boolean,
				default: true
			}
		},
		data() {
			return {
				ani: '',
				showPopup: false
			}
		},
		watch: {
			show(newValue) {
				if (newValue) {
					this.open()
				} else {
					this.close()
				}
			}
		},
		created() {
		},
		methods: {
			clear() {},
			open() {
				this.$emit('change', {
					show: true
				})
				this.showPopup = true
				this.$nextTick(() => {
					setTimeout(() => {
						this.ani = '' + this.type
					}, 30)
				})
			},
			close(type) {
				if (!this.maskClick && type) return
				this.$emit('change', {
					show: false
				})
				this.ani = ''
				this.$nextTick(() => {
					setTimeout(() => {
						this.showPopup = false
					}, 300)
				})
			}
		}
	}
</script>
<style scoped>
	.popup {
		width: 100%;
		height: 100%;
		position: fixed;

		top: 0;
		bottom: 0;
		left: 0;
		right: 0;
		z-index: 1024;
		overflow: hidden
	}

	.popup__mask {
		position: absolute;
		top: 0;
		bottom: 0;
		left: 0;
		right: 0;
		z-index: 1024;
		background: rgba(0, 0, 0, .8);
		opacity: 0
	}



	.popup__mask.bottom,
	.popup__mask.right,
	.popup__mask.left,
	.popup__mask.center,
	.popup__mask.Top {
		opacity: 1
	}

	.popup__wrapper {
		position: absolute;
		z-index: 1025;
		box-sizing: border-box
	}

	.popup__wrapper.ani {
		transition: all .3s
	}

	.popup__wrapper.Top {
		top: 0;
		left: 0;
		width: 100%;
		transform: translateY(-100%)
	}

	.popup__wrapper.bottom {
		bottom: 0;
		left: 0;
		width: 100%;
		transform: translateY(100%)
	}
	.popup__wrapper.right {
		top: 0;
		right: 0;
		width: 100%;
		transform: translateX(100%)
	}
	.popup__wrapper.left {
		top: 0;
		left: 0;
		width: 100%;
		transform: translateX(-100%)
	}

	.popup__wrapper.center {
		width: 100%;
		height: 100%;
		display: flex;
		justify-content: center;
		align-items: center;
		transform: scale(1.2);
		opacity: 0;
	}
	.popup__mask.ani {
		transition: all .3s
	}

	.popup__wrapper-box {
		/* width: inherit; */
		/* height: 100%; */
		position: relative;
		box-sizing: border-box
	}

	.popup__wrapper.custom .popup__wrapper-box {
		/* padding: 60px; */
		background: #fff
	}

	.popup__wrapper.custom.center .popup__wrapper-box {
		position: relative;
		/* max-width: 80%;
		max-height: 80%; */
		/* overflow-y: scroll */
	}

	.popup__wrapper.custom.bottom .popup__wrapper-box,
	.popup__wrapper.custom.Top .popup__wrapper-box {
		/* width: 100%; */
		/* max-height: 1000px;
		overflow-y: scroll */
	}

	.popup__wrapper.bottom,
	.popup__wrapper.Top {
		transform: translateY(0);
		z-index: 1024;
	}

	.popup__wrapper.right{
		transform: translateX(0)
	}

	.popup__wrapper.left{
		transform: translateX(0)
	}


	.popup__wrapper.center {
		transform: scale(1);
		opacity: 1
	}
</style>
