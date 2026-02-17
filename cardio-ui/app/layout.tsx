export const metadata = {
    title: "CardioSphere Intelligence",
    description: "Swarm Cognitive Engine",
};

export default function RootLayout({
    children,
}: {
    children: React.ReactNode;
}) {
    return (
        <html lang="en">
            <body style={{ margin: 0 }}>
                {children}
            </body>
        </html>
    );
}
