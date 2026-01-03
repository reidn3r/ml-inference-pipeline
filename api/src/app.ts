import "reflect-metadata"
import Fastify from "fastify"
import { serializerCompiler, validatorCompiler } from "fastify-type-provider-zod";
import { InferenceController } from "./routes/inference.controller";
import { HealthCheckController } from "./routes/health.controller";

export const app = Fastify()

//Zod
app.setValidatorCompiler(validatorCompiler);
app.setSerializerCompiler(serializerCompiler);

//Endpoints
app.register(HealthCheckController, { prefix: "health"});
app.register(InferenceController, { prefix: "inference"});
