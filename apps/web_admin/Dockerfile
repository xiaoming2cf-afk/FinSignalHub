FROM node:24-alpine

WORKDIR /app

COPY apps/web_admin/package.json apps/web_admin/package-lock.json ./apps/web_admin/
RUN npm --prefix apps/web_admin --workspaces=false ci

COPY apps/web_admin ./apps/web_admin
RUN npm --prefix apps/web_admin --workspaces=false run build

EXPOSE 3000

CMD ["npm", "--prefix", "apps/web_admin", "--workspaces=false", "run", "start"]
