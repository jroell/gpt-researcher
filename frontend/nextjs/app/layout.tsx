import type { Metadata } from "next";
import { Lexend } from "next/font/google";
import PlausibleProvider from "next-plausible";
import "./globals.css";

const inter = Lexend({ subsets: ["latin"] });

let title = "Vurvey Researcher";
let description = "A research assistant vanquishing hallucinations";
let url = "https://vurvey.com";
let ogimage = "/favicon.ico";
let sitename = "Vurvey Researcher";

export const metadata: Metadata = {
  metadataBase: new URL(url),
  title,
  description,
  icons: {
    icon: "/favicon.ico",
  },
  openGraph: {
    images: [ogimage],
    title,
    description,
    url: url,
    siteName: sitename,
    locale: "en_US",
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    images: [ogimage],
    title,
    description,
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <head>
        <PlausibleProvider domain="localhost:3000" />
      </head>
      <body
        className={`${inter.className} gradient flex min-h-screen flex-col justify-between`}
      >
        {children}
      </body>
    </html>
  );
}
