<template>
	<div class="flex h-screen w-screen">
		<SideBar />
		<router-view class="z-0 grow overflow-auto" />
	</div>
</template>

<script setup lang="ts">
import { onBeforeMount } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "@/stores/auth";
import { useConfigStore } from "@/stores/config";
import { CUSTOMER_PORTAL_LANDING, ONBOARDING_PAGE } from "@/router";
import SideBar from "@/components/desk/sidebar/SideBar.vue";

const router = useRouter();
const authStore = useAuthStore();
const configStore = useConfigStore();

onBeforeMount(() => {
	if (!authStore.hasDeskAccess) {
		router.replace({ name: CUSTOMER_PORTAL_LANDING });
	}

	if (!configStore.isSetupComplete) {
		router.replace({ name: ONBOARDING_PAGE });
	}
});
</script>
