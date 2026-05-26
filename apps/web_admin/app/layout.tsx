import "./globals.css";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "FinSignalHub Admin Scaffold",
  description: "Stage 01 inspect-only scaffold status"
};

export default function RootLayout({
  children
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}

