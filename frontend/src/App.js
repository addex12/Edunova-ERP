import { QueryClientProvider } from "@tanstack/react-query";
import { Routes, Route } from "wouter"; // Changed from Switch
import { queryClient } from "./lib/queryClient";
import { Toaster } from "@/components/ui/toaster";
import { AuthProvider } from "@/hooks/use-auth";
import NotFound from "@/pages/not-found";
import AuthPage from "@/pages/auth-page";
import DashboardPage from "@/pages/dashboard-page";
import { ProtectedRoute } from "./lib/protected-route";
import LoginPage from "@/pages/login-page"; // Added Login Page

function Router() {
  return (
    <Routes>
      <ProtectedRoute path="/" component={DashboardPage} />
      <Route path="/auth" component={AuthPage} />
      <Route path="/login" component={LoginPage} /> {/* Added Login route */}
      <Route component={NotFound} />
    </Routes>
  );
}

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <AuthProvider>
        <Router />
        <Toaster />
      </AuthProvider>
    </QueryClientProvider>
  );
}

export default App;
